from dataclasses import dataclass


@dataclass
class FaceBox:
    t: float
    x: int
    y: int
    w: int
    h: int


def smooth_track(boxes: list[FaceBox], alpha: float = 0.7) -> list[FaceBox]:
    if not boxes:
        return []
    smoothed = [boxes[0]]
    for b in boxes[1:]:
        prev = smoothed[-1]
        smoothed.append(
            FaceBox(
                t=b.t,
                x=int(alpha * prev.x + (1 - alpha) * b.x),
                y=int(alpha * prev.y + (1 - alpha) * b.y),
                w=int(alpha * prev.w + (1 - alpha) * b.w),
                h=int(alpha * prev.h + (1 - alpha) * b.h),
            )
        )
    return smoothed
