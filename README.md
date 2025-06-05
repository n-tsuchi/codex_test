Readme!!

## audio_mosaic.py

This script divides an audio file into small chunks and shuffles them to make the speech unrecognizable while preserving voice characteristics.

Usage:
```bash
python audio_mosaic.py input.wav output.wav --chunk_ms 100
```

## Installation

Install the Python dependencies with pip:

```bash
pip install -r requirements.txt
```

`pydub` relies on `ffmpeg`, so ensure it is available on your system.
