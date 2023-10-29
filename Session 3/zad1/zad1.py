import os
import shutil

def create_copy_folder():
    try:
        os.makedirs('copy')
        return True
    except FileExistsError:
        print("Folder 'copy' already exists")
        return False

def show_files(folder_names):
    paths_of_files = []

    for folder_name in folder_names:
        folder_path = os.path.join('.', folder_name)
        if os.path.isdir(folder_path):
            files_in_folder = os.listdir(folder_path)
            allowed_extensions = ('.jpg', '.JPG', '.png', '.PNG')
            for file in files_in_folder:
                if file.lower().endswith(allowed_extensions):
                    file_path = os.path.join(folder_path, file)
                    paths_of_files.append(file_path)

    return paths_of_files

def copy_photo_files(paths_of_files):
    try:
        for file_path in paths_of_files:
            file_name = os.path.basename(file_path)
            destination = os.path.join('copy', file_name)
            shutil.copy(file_path, destination)
    except (FileExistsError, shutil.SameFileError) as e:
        print(f"An error occurred while copying the files: {e}")

folders_to_show = ('holidays', 'trip', 'winter')

if create_copy_folder():
    file_paths = show_files(folders_to_show)
    print("Folder 'copy' was created, files were copied.")
    if not file_paths:
        print("There were no photos to copy")
    else:
        copy_photo_files(file_paths)
        print("Copied files list:")
        for path in file_paths:
            print(path)
else:
    exit()
