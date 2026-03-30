from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.auth.deps import get_current_user
from app.db.session import get_db
from app.models.models import ProcessingStatus, Subscription, User, Video
from app.schemas.video import VideoOut
from app.services.media import probe_video
from app.services.usage import assert_upload_quota
from workers.tasks import process_video_pipeline

router = APIRouter(prefix='/videos', tags=['videos'])
ALLOWED = {'.mp4', '.mov', '.mkv'}


@router.get('', response_model=list[VideoOut])
def list_videos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Video).filter(Video.user_id == current_user.id).order_by(Video.created_at.desc()).all()


@router.post('/upload', response_model=VideoOut)
def upload_video(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ext = Path(file.filename or '').suffix.lower()
    if ext not in ALLOWED:
        raise HTTPException(status_code=400, detail='Unsupported file type')

    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    assert sub is not None
    try:
        assert_upload_quota(sub)
    except ValueError as exc:
        raise HTTPException(status_code=402, detail=str(exc)) from exc

    out_name = f"{uuid4()}{ext}"
    out_dir = Path('uploads')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / out_name
    out_path.write_bytes(file.file.read())

    meta = probe_video(str(out_path))
    video = Video(
        user_id=current_user.id,
        title=Path(file.filename or 'Untitled').stem,
        original_filename=file.filename or out_name,
        stored_path=str(out_path),
        duration_seconds=meta['duration'],
        width=meta['width'],
        height=meta['height'],
        file_size=meta['size'],
        processing_status=ProcessingStatus.PENDING,
    )
    sub.uploads_used_period += 1
    db.add(video)
    db.commit()
    db.refresh(video)

    process_video_pipeline.delay(video.id, current_user.id)
    return video
