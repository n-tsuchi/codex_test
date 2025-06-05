"""
Audio mosaic script: scramble audio to obscure speech while keeping voice characteristics.
"""

import random
from pydub import AudioSegment


def audio_mosaic(input_file: str, output_file: str, chunk_ms: int = 100) -> None:
    """Apply mosaic effect by shuffling small chunks of audio."""
    audio = AudioSegment.from_file(input_file)
    chunks = []
    for start in range(0, len(audio), chunk_ms):
        end = start + chunk_ms
        chunk = audio[start:end]
        chunks.append(chunk)
    random.shuffle(chunks)
    mosaic_audio = sum(chunks)
    mosaic_audio.export(output_file, format="wav")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Add mosaic effect to audio")
    parser.add_argument("input", help="Input audio file")
    parser.add_argument("output", help="Output audio file")
    parser.add_argument("--chunk_ms", type=int, default=100, help="Chunk length in ms")
    args = parser.parse_args()
    audio_mosaic(args.input, args.output, args.chunk_ms)
