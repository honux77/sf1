import os

def convert_encoding(file_path, src_encoding='cp949', dest_encoding='utf-8'):
    with open(file_path, 'r', encoding=src_encoding) as file:
        content = file.read()
    with open(file_path, 'w', encoding=dest_encoding) as file:
        file.write(content)

def convert_all_html_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    convert_encoding(file_path)
                    print(f"Converted: {file_path}")
                except Exception as e:
                    print(f"Failed to convert {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_all_html_files_in_directory(current_directory)
