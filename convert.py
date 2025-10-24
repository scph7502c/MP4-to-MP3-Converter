import os
import sys
from pydub import AudioSegment


def convert_mp4_to_mp3(mp4_path, mp3_path):
    try:
        audio = AudioSegment.from_file(mp4_path, format="mp4")
        audio = audio.set_frame_rate(16000)
        audio.export(mp3_path, format="mp3")
        print(f"Conversion successful: {mp3_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file.mp4> <output_file.mp3>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    convert_mp4_to_mp3(input_file, output_file)
