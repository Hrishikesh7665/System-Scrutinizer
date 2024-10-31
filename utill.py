import os,sys
import hashlib

def current_path():
    CurrentPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(CurrentPath)
    newPath = path.replace(os.sep, '\\')
    return newPath

def hash_folder(folder):
    if not os.path.exists(folder):
        return False
    sha256 = hashlib.sha256()
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    sha256.update(data)
    calculated_hash = sha256.hexdigest()
    return calculated_hash

print(hash_folder('C:\\Users\\Hrishikesh\\Desktop\\System-Scrutinizer\\System Report\\assets'))


def zip_to_binary(zip_file_path):
    with open(zip_file_path, 'rb') as file:
        binary_content = file.read()
    return binary_content

# Example usage
# binary_data = zip_to_binary('assets.zip')
# print (binary_data)