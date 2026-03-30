from ai.scoring.virality import virality_score
from ai.story_arc.detector import arc_completeness_score, detect_story_arc


def build_candidates(segments: list[dict]) -> list[dict]:
    arcs = detect_story_arc(segments)
    candidates: list[dict] = []
    window_size = 5
    for i in range(0, len(segments), window_size):
        batch = segments[i : i + window_size]
        if not batch:
            continue
        text = ' '.join(s.get('text', '').strip() for s in batch).strip()
        local_arc = arcs[i : i + window_size]
        story_score = arc_completeness_score(local_arc)
        viral = virality_score(text, story_score)
        final = round((viral * 0.75) + (story_score * 0.25), 2)
        candidates.append(
            {
                'start_time': batch[0].get('start', 0),
                'end_time': batch[-1].get('end', 0),
                'candidate_title': (text[:72] + '...') if len(text) > 72 else text,
                'transcript_snippet': text,
                'virality_score': viral,
                'story_arc_score': story_score,
                'final_score': final,
            }
        )
    return sorted(candidates, key=lambda c: c['final_score'], reverse=True)
