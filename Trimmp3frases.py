from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os

def process_audio(file_path, attack_threshold=-40.00, release_threshold=-34.00, fade_in_ms=20, fade_out_ms=20, min_silence_len=300):
    """
    Process a single MP3 file: trim silence, add fade-in/out, and return the processed AudioSegment.
    """
    # Load the audio file
    audio = AudioSegment.from_file(file_path, format="mp3")

    # Detect non-silent parts (returns list of [start, end] in ms)
    nonsilent_ranges = detect_nonsilent(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=attack_threshold
    )

    # Concatenate non-silent parts
    processed_audio = AudioSegment.empty()
    for start, end in nonsilent_ranges:
        segment = audio[start:end]
        segment = segment.fade_in(fade_in_ms).fade_out(fade_out_ms)
        processed_audio += segment

    return processed_audio

def process_all_mp3s_in_folder(folder_path):
    """
    Process all MP3 files in the given folder and save each processed file in an "output" subfolder.
    """
    # List all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

    # Create an output folder
    output_folder = os.path.join(folder_path, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Process each MP3 file
    for mp3_file in mp3_files:
        file_path = os.path.join(folder_path, mp3_file)
        print(f"Processing: {mp3_file}")
        processed_audio = process_audio(file_path)

        # Save the processed file in the output folder
        output_path = os.path.join(output_folder, mp3_file)
        processed_audio.export(output_path, format="mp3")
        print(f"Processed file saved to: {output_path}")

# Run the script
if __name__ == "__main__":
    folder_path = os.getcwd()  # Use the current folder
    process_all_mp3s_in_folder(folder_path)
