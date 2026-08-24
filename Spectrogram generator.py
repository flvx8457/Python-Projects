import os
import numpy as np
import librosa
import librosa.display
import matplotlib
matplotlib.use("Agg")  # ensures window display works on Linux/Chromebook
import matplotlib.pyplot as plt


# -----------------------------
# LOAD AUDIO
# -----------------------------
def load_audio(file_path, target_sr=32000):
    """Load audio file and standardize sample rate"""
    try:
        y, sr = librosa.load(file_path, sr=target_sr)

        print(f"\nLoaded: {file_path}")
        print(f"Sample rate: {sr}")
        print(f"Duration: {len(y)/sr:.2f} seconds")

        return y, sr

    except Exception as e:
        print(f"Error loading audio: {e}")
        return None, None


# -----------------------------
# CREATE + SHOW + SAVE SPECTROGRAM
# -----------------------------
def create_spectrogram(y, sr, output_path=None, title="Spectrogram"):
    """Generate mel spectrogram, display it, and optionally save it"""

    # Convert audio → mel spectrogram
    S = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_mels=128,
        fmax=16000
    )

    # Convert power → decibels
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Plot
    plt.figure(figsize=(10, 5))

    librosa.display.specshow(
        S_dB,
        sr=sr,
        x_axis='time',
        y_axis='mel'
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title(title)
    plt.tight_layout()

    # SAVE IMAGE (for ML dataset)
    if output_path:
        plt.savefig(output_path, bbox_inches="tight", pad_inches=0)

    # SHOW IMAGE (for viewing)
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0)
plt.close()


# -----------------------------
# OPTIONAL: FIX LENGTH (VERY IMPORTANT FOR ML)
# -----------------------------
def fix_length(y, sr, seconds=5):
    """Trim or pad audio to fixed length"""
    target_len = seconds * sr

    if len(y) > target_len:
        y = y[:target_len]
    else:
        y = np.pad(y, (0, target_len - len(y)))

    return y


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("🎧 Audio → Spectrogram Converter (ML Ready)\n")

    file_path = input("Enter audio file name (.wav or .mp3): ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found. Put it in the same folder as this script.")
        return

    # Load audio
    y, sr = load_audio(file_path)

    if y is None:
        return

    # Fix length for consistency (important for training models)
    y = fix_length(y, sr, seconds=5)

    # Create output file name
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base_name}_spectrogram.png"

    # Generate spectrogram
    create_spectrogram(
        y,
        sr,
        output_path=output_file,
        title=f"Spectrogram: {base_name}"
    )

    print(f"\n✅ Saved spectrogram as: {output_file}")


if __name__ == "__main__":
    main()