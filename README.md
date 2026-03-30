# Jus Clip It

Jus Clip It is an AI-powered SaaS platform that turns long-form videos into ranked short-form clips for TikTok, Reels, and Shorts.

## Monorepo structure

- `client/` Next.js frontend (App Router + TypeScript + Tailwind)
- `server/` FastAPI backend (auth, uploads, clips, billing)
- `ai/` transcription, story arc detection, virality scoring, candidate generation
- `video_processing/` ffmpeg rendering, caption formatting, reframing engine
- `workers/` Celery queue tasks
- `database/` migration placeholders
- `docs/` architecture, API, and billing notes
- `uploads/` local source media in dev
- `clips/` rendered outputs in dev

## Local setup

### Prereqs

- Python 3.11+
- Node 20+
- PostgreSQL 16+
- Redis 7+
- FFmpeg + ffprobe installed and available in PATH

### 1) Environment

```bash
cp .env.example .env
```

### 2) Infra

```bash
docker compose up -d postgres redis
```

### 3) Backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r server/requirements.txt
uvicorn server.main:app --reload --port 8000
```

### 4) Worker

```bash
celery -A workers.tasks worker -l info
```

### 5) Frontend

```bash
cd client
npm install
npm run dev
```

## Feature coverage in MVP

- JWT authentication (register/login)
- SaaS subscriptions model (Free/Pro/Business) + usage quota checks
- Video upload with type validation and ffprobe metadata extraction
- Async job orchestration through Celery
- Whisper transcription integration
- Heuristic story arc labeling and completeness scoring
- Modular virality scoring engine with weighted signals
- Candidate clip generation and ranking by final score
- FFmpeg clip rendering and caption burn-in helper
- Smart vertical crop timeline generator for reframing
- Stripe checkout + webhook sync skeleton
- Next.js routes for landing/auth/dashboard/video/clip/billing

## Notes

This is a production-minded MVP baseline intended for local dev and staged cloud hardening. Storage adapters (S3), stronger refresh-token flows, multi-tenant team support, advanced CV/LLM scoring, and robust observability are designed to be added incrementally.
