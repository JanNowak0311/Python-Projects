import os
import shutil

path = "your/folder/path"  # Change this to your folder path
files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        if not os.path.exists("Text"):
            os.makedirs("Text")
        shutil.move(os.path.join(path, file), os.path.join(path, "Text", file))
    elif file.endswith(".jpg"):
        if not os.path.exists("Images"):
            os.makedirs("Images")
        shutil.move(os.path.join(path, file), os.path.join(path, "Images", file))
print("Files organized")
