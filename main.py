import wave
import struct

# Open the audio file
audio_path = 'file.wav'
with wave.open(audio_path, 'rb') as audio_file:
    # Get the number of frames (samples)
    num_frames = audio_file.getnframes()

    # Set the chunk size
    chunk_size = 1024

    # Initialize list to store amplitudes
    amplitudes = []

    # Read and process audio data in chunks
    while True:
        frames = audio_file.readframes(chunk_size)
        if not frames:
            break
        # Convert binary data to a list of amplitude values
        # Assuming the audio file is in 16-bit PCM format
        # You might need to adjust this based on the format of your audio file
        amplitudes.extend(struct.unpack(f'{len(frames)//2}h', frames))

# Map the amplitudes directly to the values
mapped_values = [abs(value) for value in amplitudes]

print("Mapped waveform values:", mapped_values)

