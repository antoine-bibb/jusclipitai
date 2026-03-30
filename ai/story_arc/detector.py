from dataclasses import dataclass

LABELS = ['HOOK', 'CONTEXT', 'BUILD', 'CLIMAX', 'REACTION']


@dataclass
class ArcChunk:
    start: float
    end: float
    text: str
    label: str


def classify_chunk(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ['here is why', 'listen', 'you won\'t believe', 'first thing']):
        return 'HOOK'
    if any(k in t for k in ['because', 'the reason', 'context', 'background']):
        return 'CONTEXT'
    if any(k in t for k in ['then', 'next', 'suddenly', 'started', 'rising']):
        return 'BUILD'
    if any(k in t for k in ['boom', 'finally', 'the craziest', 'that\'s when']):
        return 'CLIMAX'
    return 'REACTION'


def detect_story_arc(segments: list[dict]) -> list[ArcChunk]:
    chunks = []
    for seg in segments:
        label = classify_chunk(seg.get('text', ''))
        chunks.append(ArcChunk(start=seg.get('start', 0), end=seg.get('end', 0), text=seg.get('text', ''), label=label))
    return chunks


def arc_completeness_score(chunks: list[ArcChunk]) -> float:
    present = {c.label for c in chunks}
    return round((len(present.intersection(set(LABELS))) / len(LABELS)) * 100, 2)
