from dataclasses import dataclass


@dataclass
class ScoreWeights:
    hook: float = 0.18
    emotional: float = 0.14
    conflict: float = 0.12
    novelty: float = 0.14
    energy: float = 0.10
    scene: float = 0.10
    speaker: float = 0.08
    story_arc: float = 0.14


def _signal_score(text: str, keywords: list[str]) -> float:
    t = text.lower()
    hits = sum(1 for k in keywords if k in t)
    return min(100, hits * 25)


def virality_score(text: str, story_arc_score: float, weights: ScoreWeights | None = None) -> float:
    w = weights or ScoreWeights()
    hook = _signal_score(text, ['wait', 'stop scrolling', 'listen', 'the truth'])
    emotional = _signal_score(text, ['amazing', 'insane', 'love', 'hate', 'crazy'])
    conflict = _signal_score(text, ['but', 'however', 'problem', 'fight', 'versus'])
    novelty = _signal_score(text, ['never', 'first time', 'secret', 'unexpected'])
    energy = _signal_score(text, ['!', 'right now', 'today'])
    scene = _signal_score(text, ['suddenly', 'then'])
    speaker = _signal_score(text, ['i', 'we', 'you'])
    final = (
        hook * w.hook
        + emotional * w.emotional
        + conflict * w.conflict
        + novelty * w.novelty
        + energy * w.energy
        + scene * w.scene
        + speaker * w.speaker
        + story_arc_score * w.story_arc
    )
    return round(min(100, final), 2)
