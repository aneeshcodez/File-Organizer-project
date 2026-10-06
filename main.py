import os
from pathlib import Path
import shutil

parent_path = "/Users/aneesh/Desktop/Sample-Folder/"

# Creating sub-folders inside the folder
sub_folder_1_name = "PDF_FOLDER"
sub_folder_2_name = "JPG_FOLDER"
sub_folder_3_name = "VIDEO_FOLDER"

target_path_1 = os.path.join(parent_path, sub_folder_1_name)
os.makedirs(target_path_1, exist_ok=True)
print(f"Folder created at: {target_path_1}")

target_path_2 = os.path.join(parent_path, sub_folder_2_name)
os.makedirs(target_path_2, exist_ok=True)
print(f"Folder created at: {target_path_2}")

target_path_3 = os.path.join(parent_path, sub_folder_3_name)
os.makedirs(target_path_3, exist_ok=True)
print(f"Folder created at: {target_path_3}")


files = os.listdir(parent_path)


for file in files:

    file_path = Path(os.path.join(parent_path, file))

    if file_path.is_file():

        if file_path.suffix == ".pdf":
            shutil.move(
                file_path,
                os.path.join(parent_path, "PDF_FOLDER", file)
            )

        elif file_path.suffix == ".jpg":
            shutil.move(
                file_path,
                os.path.join(parent_path, "JPG_FOLDER", file)
            )

        elif file_path.suffix == ".mp4":
            shutil.move(
                file_path,
                os.path.join(parent_path, "VIDEO_FOLDER", file)
            )


