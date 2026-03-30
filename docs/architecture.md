# Jus Clip It Architecture

- **client/**: Next.js app router frontend for landing, auth, dashboard, clip editor, billing.
- **server/**: FastAPI REST API with JWT auth, quotas, uploads, clips, billing webhooks.
- **ai/**: Transcription, story arc heuristics, virality scoring, clip candidate generation.
- **video_processing/**: ffmpeg rendering helpers, subtitle formatting, reframe crop path logic.
- **workers/**: Celery background processing pipeline for non-blocking media jobs.
- **database/**: migration/seed placeholders for evolution with Alembic.
