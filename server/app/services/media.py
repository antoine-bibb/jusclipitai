import json
import subprocess
from pathlib import Path

from app.core.config import settings


def probe_video(path: str) -> dict:
    cmd = [
        settings.ffprobe_bin,
        '-v',
        'error',
        '-print_format',
        'json',
        '-show_streams',
        '-show_format',
        path,
    ]
    out = subprocess.check_output(cmd, text=True)
    data = json.loads(out)
    video_stream = next((s for s in data['streams'] if s.get('codec_type') == 'video'), {})
    return {
        'duration': float(data['format'].get('duration', 0)),
        'width': int(video_stream.get('width', 0) or 0),
        'height': int(video_stream.get('height', 0) or 0),
        'size': int(data['format'].get('size', 0) or Path(path).stat().st_size),
    }
