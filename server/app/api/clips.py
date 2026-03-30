from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.deps import get_current_user
from app.db.session import get_db
from app.models.models import CaptionStyle, Clip, User

router = APIRouter(prefix='/clips', tags=['clips'])


@router.get('/video/{video_id}')
def clips_by_video(video_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return (
        db.query(Clip)
        .filter(Clip.video_id == video_id, Clip.user_id == current_user.id)
        .order_by(Clip.final_score.desc())
        .all()
    )


@router.patch('/{clip_id}/caption-style')
def update_caption_style(
    clip_id: int,
    settings_json: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    clip = db.query(Clip).filter(Clip.id == clip_id, Clip.user_id == current_user.id).first()
    if not clip:
        raise HTTPException(status_code=404, detail='Clip not found')

    style = db.query(CaptionStyle).filter(CaptionStyle.clip_id == clip.id).first()
    if not style:
        style = CaptionStyle(clip_id=clip.id, settings_json=settings_json)
        db.add(style)
    else:
        style.settings_json = settings_json
    db.commit()
    return {'ok': True}
