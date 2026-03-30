from datetime import datetime

from pydantic import BaseModel


class VideoOut(BaseModel):
    id: int
    title: str
    duration_seconds: float
    processing_status: str
    created_at: datetime

    class Config:
        from_attributes = True
