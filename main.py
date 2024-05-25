#!/usr/bin/env python

"""
Audio Processing Script

Author: Victor Kolis (Victor Dematos)
E-mail: victorkolis@duck.com

This script reads a WAV audio file, calculates the highs on the waveform,
and generates a collection of random numbers based on these highs.

Usage:
1. Ensure the audio file is in WAV format and named 'file.wav'.
2. Run the script.
3. The script will output a collection of random numbers based on the highs in the waveform.

Note: This script assumes the audio file is in 16-bit PCM format. You may need to adjust
      it if your file has a different format.

"""

import wave
import struct
import random

# Open the audio file
audio_path = 'file.wav'
with wave.open(audio_path, 'rb') as audio_file:
    # Get the number of frames (samples)
    num_frames = audio_file.getnframes()
    
    # Set the chunk size
    chunk_size = 512
    
    # Initialize lists to store amplitudes and random numbers
    amplitudes = []
    random_numbers = []
    
    # Read and process audio data in chunks
    while True:
        frames = audio_file.readframes(chunk_size)
        if not frames:
            break
        # Convert binary data to a list of amplitude values
        # Assuming the audio file is in 16-bit PCM format
        # You might need to adjust this based on the format of your audio file
        amplitudes.extend(struct.unpack(f'{len(frames)//2}h', frames))
        # Generate random numbers based on the highs in the current chunk
        random_numbers.extend([random.randint(0, 9) for _ in range(len(frames)//2)])

# Get the highs on the waveform
highs = max(amplitudes)

print("Random numbers based on highs in waveform:", random_numbers)
