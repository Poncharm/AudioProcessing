import os
from pydub import AudioSegment, effects

def normalize_audio(audio_segment):
    change_in_dBFS = -audio_segment.max_dBFS
    return audio_segment.apply_gain(change_in_dBFS)

def add_fade_effects(audio_segment, fade_duration=1000):
    return audio_segment.fade_in(fade_duration).fade_out(fade_duration)

# def ensure_mono(audio_segment):
#     if audio_segment.channels > 1:
#         return audio_segment.set_channels(1)
#     return audio_segment
#
# def set_sample_rate(audio_segment, sample_rate=44100):
#     return audio_segment.set_frame_rate(sample_rate)
#
# def apply_compression(audio_segment):
#     return effects.compress_dynamic_range(audio_segment)
#
# def remove_dc_offset(audio_segment):
#     return effects.normalize(audio_segment)
#
# def set_bit_depth(audio_segment, bit_depth=16):
#     return audio_segment.set_sample_width(bit_depth // 8)

def process_audio_files(input_folder, output_folder, fade_duration=1000):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".mp3", ".wav")):
            filepath = os.path.join(input_folder, filename)
            audio = AudioSegment.from_file(filepath)

            # # Ensure audio is mono
            # mono_audio = ensure_mono(audio)
            #
            # # Set sample rate
            # audio_with_fixed_sample_rate = set_sample_rate(mono_audio)
            #
            # # Remove DC offset
            # dc_corrected_audio = remove_dc_offset(audio_with_fixed_sample_rate)
            #
            # # Apply compression
            # compressed_audio = apply_compression(dc_corrected_audio)
            #
            # # Normalize the audio
            # normalized_audio = normalize_audio(compressed_audio)

            # Set bit depth
            # bit_depth_audio = set_bit_depth(normalized_audio)
            bit_depth_audio = audio

            # Calculate start and end for 7 second clip around the middle
            half_duration = len(bit_depth_audio) / 2
            start = half_duration - 6000
            end = half_duration + 6000
            clipped_audio = bit_depth_audio[start:end]

            # Apply fade effects
            final_audio = add_fade_effects(clipped_audio, fade_duration)

            # Export the processed audio
            output_filepath = os.path.join(output_folder, filename)
            final_audio.export(output_filepath, format="mp3")

# Define input and output folders
input_folder = "Sounds/Processed sounds/relax_natural"
output_folder = "Sounds/Cut sounds 10 sec/relax_natural"

# Process the audio files
process_audio_files(input_folder, output_folder)
