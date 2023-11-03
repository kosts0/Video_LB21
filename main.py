import ffmpeg
import os
from pathlib import Path


def main(input_video_path, output_video_path, audio_input):
    print(os.path.isfile(input_video_path))
    video_duration = duration = ffmpeg.probe(input_video_path)["format"]["duration"]
    in_video = ffmpeg.input(input_video_path)
    in_video = ffmpeg.hflip(in_video)
    if audio_input is not None:
        in_audio = ffmpeg.input(audio_input)
        in_audio = ffmpeg.filter(in_audio, 'atrim', duration=video_duration)
        ffmpeg.run(ffmpeg.output(in_video, in_audio, output_video_path))
    else:
        in_video = ffmpeg.output(in_video, output_video_path)
        ffmpeg.run(in_video)


if __name__ == '__main__':
    import sys

    print(sys.argv)
    input_video_path = sys.argv[1]
    output_video_path = sys.argv[2]
    audio_input = sys.argv[3] if len(sys.argv) > 3 else None
    main(input_video_path, output_video_path, audio_input)
