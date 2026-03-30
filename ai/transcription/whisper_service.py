from functools import lru_cache

import whisper


@lru_cache
def _load_model(model_name: str = 'base'):
    return whisper.load_model(model_name)


def transcribe_video(video_path: str, model_name: str = 'base') -> dict:
    model = _load_model(model_name)
    result = model.transcribe(video_path, word_timestamps=True)
    return {
        'full_text': result.get('text', '').strip(),
        'segments': result.get('segments', []),
        'words': [w for s in result.get('segments', []) for w in s.get('words', [])],
    }
