import os
import shutil

extensions = {
    'mp4': 'Videos',
    'wmv': 'Videos',
    'mov': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'mkv': 'Videos',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'pdf': 'Documents',
    'txt': 'Documents',
    'docx': 'Documents',
    'xlsx': 'Documents',
    'pptx': 'Documents',
    'mp3': 'Music',
    'exe': 'Apps',
    'zip': 'Archives',
    'rar': 'Archives',
    '7z': 'Archives'
}

unorganized_folder = input('Enter the full path of the folder you want to organize: ')
files = os.listdir(unorganized_folder)

for file in files:
    name, extension = os.path.splitext(file)
    extension = extension[1:]

    if extension in extensions:
        subfolder = os.path.join(unorganized_folder, extensions[extension])
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        shutil.move(os.path.join(unorganized_folder, file), os.path.join(subfolder, file))

print('Done!')