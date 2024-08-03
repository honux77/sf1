import os

def rename_files_to_lowercase(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = file.lower()
            new_file_path = os.path.join(root, new_file_name)
            if old_file_path != new_file_path:
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"Failed to rename {old_file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_files_to_lowercase(current_directory)
