from ai.story_arc.detector import arc_completeness_score, detect_story_arc


def test_story_arc_scoring_has_range():
    segments = [
        {'start': 0, 'end': 2, 'text': 'Listen, here is why this works.'},
        {'start': 2, 'end': 4, 'text': 'Because context matters a lot.'},
        {'start': 4, 'end': 6, 'text': 'Then things suddenly escalated.'},
        {'start': 6, 'end': 8, 'text': "That's when the craziest part happened."},
        {'start': 8, 'end': 10, 'text': 'And everyone reacted.'},
    ]
    chunks = detect_story_arc(segments)
    score = arc_completeness_score(chunks)
    assert 0 <= score <= 100
    assert len(chunks) == 5
