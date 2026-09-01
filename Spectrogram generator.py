import os
import numpy as np
import librosa
import librosa.display
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt


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



def create_spectrogram(y, sr, output_path=None, title="Spectrogram"):
    """Generate mel spectrogram, display it, and optionally save it"""

    # Convert audio to mel spectrogram
    S = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_mels=128,
        fmax=16000
    )

   
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


    if output_path:
        plt.savefig(output_path, bbox_inches="tight", pad_inches=0)

   
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0)
plt.close()



def fix_length(y, sr, seconds=5):
    """Trim or pad audio to fixed length"""
    target_len = seconds * sr

    if len(y) > target_len:
        y = y[:target_len]
    else:
        y = np.pad(y, (0, target_len - len(y)))

    return y



def main():
    print("🎧 Audio → Spectrogram Converter (ML Ready)\n")

    file_path = input("Enter audio file name (.wav or .mp3): ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found. Put it in the same folder as this script.")
        return

   
    y, sr = load_audio(file_path)

    if y is None:
        return

   
    y = fix_length(y, sr, seconds=5)

   
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base_name}_spectrogram.png"

    create_spectrogram(
        y,
        sr,
        output_path=output_file,
        title=f"Spectrogram: {base_name}"
    )

    print(f"\n✅ Saved spectrogram as: {output_file}")


if __name__ == "__main__":
    main()
