import enum
from datetime import datetime

from sqlalchemy import JSON, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PlanTier(str, enum.Enum):
    FREE = 'free'
    PRO = 'pro'
    BUSINESS = 'business'


class ProcessingStatus(str, enum.Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    FAILED = 'failed'


class JobType(str, enum.Enum):
    TRANSCRIBE = 'transcribe'
    DETECT_SCENES = 'detect_scenes'
    DETECT_CLIPS = 'detect_clips'
    SCORE = 'score'
    REFAME = 'reframe'
    RENDER = 'render'


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    subscription: Mapped['Subscription'] = relationship(back_populates='user', uselist=False)
    videos: Mapped[list['Video']] = relationship(back_populates='user')


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    tier: Mapped[PlanTier] = mapped_column(Enum(PlanTier), default=PlanTier.FREE)
    status: Mapped[str] = mapped_column(String(50), default='active')
    stripe_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stripe_subscription_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    current_period_start: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    current_period_end: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    clips_used_period: Mapped[int] = mapped_column(Integer, default=0)
    uploads_used_period: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship(back_populates='subscription')


class Video(Base):
    __tablename__ = 'videos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(255))
    original_filename: Mapped[str] = mapped_column(String(255))
    stored_path: Mapped[str] = mapped_column(String(1024))
    duration_seconds: Mapped[float] = mapped_column(Float, default=0)
    width: Mapped[int | None] = mapped_column(Integer, nullable=True)
    height: Mapped[int | None] = mapped_column(Integer, nullable=True)
    file_size: Mapped[int] = mapped_column(Integer)
    processing_status: Mapped[ProcessingStatus] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship(back_populates='videos')
    transcript: Mapped['Transcript'] = relationship(back_populates='video', uselist=False)
    clips: Mapped[list['Clip']] = relationship(back_populates='video')


class Transcript(Base):
    __tablename__ = 'transcripts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(ForeignKey('videos.id'), unique=True)
    full_text: Mapped[str] = mapped_column(Text)
    segments_json: Mapped[dict] = mapped_column(JSON)
    words_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    video: Mapped['Video'] = relationship(back_populates='transcript')


class Clip(Base):
    __tablename__ = 'clips'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(ForeignKey('videos.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(255))
    start_time: Mapped[float] = mapped_column(Float)
    end_time: Mapped[float] = mapped_column(Float)
    transcript_excerpt: Mapped[str] = mapped_column(Text)
    virality_score: Mapped[float] = mapped_column(Float, default=0)
    story_arc_score: Mapped[float] = mapped_column(Float, default=0)
    final_score: Mapped[float] = mapped_column(Float, default=0)
    output_path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    export_format: Mapped[str] = mapped_column(String(50), default='tiktok')
    render_status: Mapped[ProcessingStatus] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    video: Mapped['Video'] = relationship(back_populates='clips')
    caption_style: Mapped['CaptionStyle'] = relationship(back_populates='clip', uselist=False)


class CaptionStyle(Base):
    __tablename__ = 'caption_styles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    clip_id: Mapped[int] = mapped_column(ForeignKey('clips.id'), unique=True)
    settings_json: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    clip: Mapped['Clip'] = relationship(back_populates='caption_style')


class ProcessingJob(Base):
    __tablename__ = 'processing_jobs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    video_id: Mapped[int | None] = mapped_column(ForeignKey('videos.id'), nullable=True)
    clip_id: Mapped[int | None] = mapped_column(ForeignKey('clips.id'), nullable=True)
    job_type: Mapped[str] = mapped_column(String(50))
    status: Mapped[ProcessingStatus] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING)
    progress: Mapped[int] = mapped_column(Integer, default=0)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
