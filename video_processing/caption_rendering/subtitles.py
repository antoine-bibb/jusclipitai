def to_srt(segments: list[dict]) -> str:
    def fmt(sec: float) -> str:
        ms = int((sec % 1) * 1000)
        h = int(sec // 3600)
        m = int((sec % 3600) // 60)
        s = int(sec % 60)
        return f'{h:02}:{m:02}:{s:02},{ms:03}'

    lines = []
    for i, seg in enumerate(segments, start=1):
        lines.append(str(i))
        lines.append(f"{fmt(seg['start'])} --> {fmt(seg['end'])}")
        lines.append(seg.get('text', '').strip())
        lines.append('')
    return '\n'.join(lines)
