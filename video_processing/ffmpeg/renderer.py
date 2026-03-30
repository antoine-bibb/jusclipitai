import subprocess


def render_clip(input_path: str, output_path: str, start: float, end: float):
    cmd = [
        'ffmpeg', '-y', '-ss', str(start), '-to', str(end), '-i', input_path,
        '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', output_path,
    ]
    subprocess.run(cmd, check=True)


def burn_captions(input_path: str, srt_path: str, output_path: str):
    cmd = ['ffmpeg', '-y', '-i', input_path, '-vf', f'subtitles={srt_path}', '-c:a', 'copy', output_path]
    subprocess.run(cmd, check=True)
