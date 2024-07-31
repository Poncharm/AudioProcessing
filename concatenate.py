import os
import random
from pydub import AudioSegment


def create_big_audio(input_folder, output_file, overlap_duration=1000):
    combined = None
    files = [f for f in os.listdir(input_folder) if f.endswith((".mp3", ".wav"))]

    # Randomly shuffle the list of files
    random.shuffle(files)

    for filename in files:
        filepath = os.path.join(input_folder, filename)
        audio = AudioSegment.from_file(filepath)

        if combined is None:
            combined = audio
        else:
            combined = combined.append(audio, crossfade=overlap_duration)

    combined.export(output_file, format="mp3")


# Define input folder and output file
input_folder = "Sounds/Selected feedback sounds 10 sec"
output_file = "combined_audio_10_sec.mp3"

# Create the big audio file
create_big_audio(input_folder, output_file)
