import os
import random
import shutil


def select_and_copy_files(input_folders, output_folder, num_files_per_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    file_counter = 1
    used_files = set()

    for folder, num_files in zip(input_folders, num_files_per_folder):
        files = [f for f in os.listdir(folder) if f.endswith((".mp3", ".wav"))]
        # Ensure we have enough unique files to select
        if len(files) < num_files:
            raise ValueError(f"Not enough files in folder {folder} to select {num_files} unique files.")

        selected_files = set()
        while len(selected_files) < num_files:
            file = random.choice(files)
            if file not in used_files:
                selected_files.add(file)
                used_files.add(file)

        for file in selected_files:
            src_path = os.path.join(folder, file)
            # Extract the original filename without the leading number
            original_name_part = '-'.join(file.split('-')[1:])
            new_filename = f"{file_counter}-{original_name_part}"
            dst_path = os.path.join(output_folder, new_filename)

            shutil.copy(src_path, dst_path)
            file_counter += 1


# Define input folders and the number of files to select from each
input_folders = [
    "Sounds/Cut sounds 10 sec/neutral",
    "Sounds/Cut sounds 10 sec/relax_natural",
    "Sounds/Cut sounds 10 sec/relax_synthesized",
    "Sounds/Cut sounds 10 sec/stress",
    "Sounds/Cut sounds 10 sec/classic"
]
num_files_per_folder = [7, 7, 7, 7, 7]

# Define output folder
output_folder = "Sounds/Selected 35 feedback sounds 10 sec"

# Select and copy files
select_and_copy_files(input_folders, output_folder, num_files_per_folder)
