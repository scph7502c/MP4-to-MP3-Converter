# MP4 to MP3 Converter

A simple Python script that converts an MP4 video file into an MP3 audio file using [pydub](https://github.com/jiaaro/pydub).

---

## Requirements

- Python 3.8+
- `pydub` library
- `ffmpeg` installed and available in your system's PATH

Install the required Python package:

```bash
pip install pydub
```

Installing FFmpeg
On Ubuntu/Debian:
```bash
sudo apt install ffmpeg
```

On macOS (with Homebrew):
```bash
brew install ffmpeg
```

On Windows:

Download FFmpeg from https://ffmpeg.org/download.html
,
extract it, and add the bin folder to your system PATH.

**Usage**

Run the script from your terminal:

python convert.py input.mp4 output.mp3

Example
```bash
python convert.py lecture.mp4 lecture_audio.mp3
```

If the input file exists and conversion succeeds, the script will display:

```bash
Conversion successful: lecture_audio.mp3
```


If any error occurs, it will print the error message and exit with code 1.

**Conversion Details**

*Input format:* .mp4

*Output format:* .mp3

Sample rate: 16,000 Hz
