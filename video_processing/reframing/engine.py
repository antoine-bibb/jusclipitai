def compute_vertical_crop_path(
    frame_width: int,
    frame_height: int,
    face_track: list[dict],
    target_width: int = 1080,
    target_height: int = 1920,
) -> list[dict]:
    crop_w = int(frame_height * (target_width / target_height)) if frame_height else frame_width
    crop_w = min(crop_w, frame_width)

    path = []
    for p in face_track:
        center_x = p.get('x', frame_width // 2)
        x = max(0, min(frame_width - crop_w, int(center_x - crop_w / 2)))
        path.append({'time': p.get('t', 0), 'x': x, 'y': 0, 'w': crop_w, 'h': frame_height})

    if not path:
        path.append({'time': 0, 'x': (frame_width - crop_w) // 2, 'y': 0, 'w': crop_w, 'h': frame_height})
    return path
