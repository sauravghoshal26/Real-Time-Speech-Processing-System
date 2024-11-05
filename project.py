# imports.py
import os
import json
import subprocess
import librosa
import torchaudio
import soundfile as sf
import asyncio
import websockets
from monotonic_align import monotonic_align
from sklearn.model_selection import train_test_split
from IPython.display import Audio

# Define directories for audio data and manifest file
AUDIO_DIR = "/Users/sauravghoshal/Desktop/Peritys/svarah/audio"  # Update to your specific path
MANIFEST_PATH = "/Users/sauravghoshal/Desktop/Peritys/svarah/svarah_manifest.json"  # Update to your specific path
TRAIN_SCRIPT_PATH = "/Users/sauravghoshal/Desktop/Peritys/vits/train.py"
CONFIG_PATH = "/Users/sauravghoshal/Desktop/Peritys/vits/configs/base.json"
MODEL_SAVE_DIR = "/Users/sauravghoshal/Desktop/Peritys/vits/saved_model"

# Data Preparation
audio_files = [os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR) if f.endswith('.wav')]
transcripts = []

# Load transcripts from the JSON manifest
with open(MANIFEST_PATH, 'r') as f:
    for line in f:
        try:
            item = json.loads(line)
            audio_filepath = item['audio_filepath']
            transcript = item['text']
            transcripts.append((audio_filepath, transcript))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Ensure audio files are aligned with transcripts
audio_file_dict = {os.path.basename(f): f for f in audio_files}
transcripts_filtered = [
    (audio_file_dict[os.path.basename(audio_filepath)], transcript) 
    for audio_filepath, transcript in transcripts 
    if os.path.basename(audio_filepath) in audio_file_dict
]

# Split into train, validation, test sets (80/10/10)
train_files, test_files, train_transcripts, test_transcripts = train_test_split(
    [x[0] for x in transcripts_filtered], 
    [x[1] for x in transcripts_filtered], 
    test_size=0.2, 
    random_state=42
)
val_files, test_files, val_transcripts, test_transcripts = train_test_split(
    test_files, test_transcripts, 
    test_size=0.5, 
    random_state=42
)

# Print dataset split summary
print(f'Training files: {len(train_files)}, Validation files: {len(val_files)}, Test files: {len(test_files)}')

# Model Training
print("Starting training...")
subprocess.run([
    "python", TRAIN_SCRIPT_PATH, 
    "-c", CONFIG_PATH, 
    "-m", MODEL_SAVE_DIR
])
print("Training completed.")

# Define a sample rate to use for audio playback
SAMPLE_RATE = 22050

# Load and play a sample audio file from the test set for verification
sample_audio, _ = librosa.load(test_files[0], sr=SAMPLE_RATE)
# Save the audio instead of displaying it directly
sf.write("/Users/sauravghoshal/Desktop/Peritys/sample_test_output.wav", sample_audio, SAMPLE_RATE)
print("Sample audio saved to /Users/sauravghoshal/Desktop/Peritys/sample_test_output.wav")

# WebSocket Server for Streaming WAV to FLAC
async def audio_handler(websocket, path):
    async for message in websocket:
        flac_path = "/Users/sauravghoshal/Desktop/Peritys/output.flac"
        sf.write(file=flac_path, data=message, samplerate=SAMPLE_RATE, format='FLAC')
        with open(flac_path, "rb") as flac_file:
            flac_data = flac_file.read()
            await websocket.send(flac_data)

async def start_server():
    port = 8765
    server_started = False

    while not server_started:
        try:
            server = await websockets.serve(audio_handler, "127.0.0.1", port)
            server_started = True
            print(f"Server started on port {port}")
        except OSError as e:
            if e.errno == 98:
                print(f"Port {port} is in use. Trying next port...")
                port += 1
            else:
                raise e

    await server.wait_closed()

# Run the WebSocket server in the event loop
print("Starting WebSocket server...")
asyncio.run(start_server())


