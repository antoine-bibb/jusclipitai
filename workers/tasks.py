from pathlib import Path

from ai.clip_detection.candidates import build_candidates
from ai.transcription.whisper_service import transcribe_video
from app.db.session import SessionLocal
from app.models.models import Clip, ProcessingStatus, Transcript, Video
from video_processing.ffmpeg.renderer import render_clip
from workers.celery_app import app


@app.task
def process_video_pipeline(video_id: int, user_id: int):
    db = SessionLocal()
    try:
        video = db.query(Video).filter(Video.id == video_id, Video.user_id == user_id).first()
        if not video:
            return
        video.processing_status = ProcessingStatus.PROCESSING
        db.commit()

        tx = transcribe_video(video.stored_path)
        transcript = Transcript(video_id=video.id, full_text=tx['full_text'], segments_json=tx['segments'], words_json=tx['words'])
        db.add(transcript)
        db.commit()

        candidates = build_candidates(tx['segments'])
        clips_dir = Path('clips')
        clips_dir.mkdir(exist_ok=True)
        for idx, c in enumerate(candidates[:5], start=1):
            out = clips_dir / f'video_{video.id}_clip_{idx}.mp4'
            render_clip(video.stored_path, str(out), c['start_time'], c['end_time'])
            db.add(
                Clip(
                    video_id=video.id,
                    user_id=user_id,
                    title=c['candidate_title'] or f'Clip {idx}',
                    start_time=c['start_time'],
                    end_time=c['end_time'],
                    transcript_excerpt=c['transcript_snippet'],
                    virality_score=c['virality_score'],
                    story_arc_score=c['story_arc_score'],
                    final_score=c['final_score'],
                    output_path=str(out),
                    render_status=ProcessingStatus.COMPLETED,
                )
            )
        video.processing_status = ProcessingStatus.COMPLETED
        db.commit()
    except Exception as exc:  # noqa: BLE001
        if video:
            video.processing_status = ProcessingStatus.FAILED
            db.commit()
        raise exc
    finally:
        db.close()
