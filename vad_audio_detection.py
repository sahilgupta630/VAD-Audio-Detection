import argparse
import torch
import matplotlib.pyplot as plt
from silero_vad import load_silero_vad, read_audio, get_speech_timestamps

def detect_speech(audio_path):
    print(f"Loading Silero VAD model...")
    model = load_silero_vad()
    
    print(f"Reading audio file: {audio_path}")
    try:
        wav = read_audio(audio_path)
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return None

    print("Detecting speech timestamps...")
    speech_timestamps = get_speech_timestamps(
        wav,
        model,
        return_seconds=True,  # Return speech timestamps in seconds
    )
    
    print("Speech Timestamps:", speech_timestamps)
    return speech_timestamps

def plot_timestamps(speech_timestamps):
    if not speech_timestamps:
        print("No speech detected or timestamps is empty.")
        return

    fig, ax = plt.subplots(figsize=(15, 3))

    for i, ts in enumerate(speech_timestamps):
        ax.hlines(y=0.5, xmin=ts['start'], xmax=ts['end'], linewidth=5, color='blue', label='Speech' if i == 0 else "")

    ax.set_yticks([]) # Remove y-axis ticks as it's a single timeline
    ax.set_xlabel('Time (seconds)')
    ax.set_title('Speech Activity Timeline')
    ax.set_xlim(0, max(ts['end'] for ts in speech_timestamps) + 2) # Adjust x-axis limit for better visualization
    
    # Avoid duplicate labels in legend
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        ax.legend(handles, labels, loc='upper right')
        
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Voice Activity Detection (VAD) using Silero VAD")
    parser.add_argument("--audio", type=str, default="Recording.m4a", help="Path to the audio file")
    
    args = parser.parse_args()
    
    timestamps = detect_speech(args.audio)
    if timestamps:
         plot_timestamps(timestamps)

if __name__ == "__main__":
    main()