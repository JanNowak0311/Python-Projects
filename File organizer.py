import os
import shutil

print("To exit the app just type in 'out'")
while True:
    path = input("Type in your folder path (e.g. 'your/folder/path') ")
    if path == "out":
        print("Goodbye")
        break
    else:
        if not os.path.isdir(path):
            print("Invalid path! Please enter a valid folder path.")
            continue
        files = os.listdir(path)
        for file in files:
            if file.endswith(".txt"):
                if not os.path.exists(os.path.join(path, "Text")):
                    os.makedirs(os.path.join(path, "Text"))
                shutil.move(os.path.join(path, file), os.path.join(path, "Text", file))
            elif file.endswith(".jpg"):
                if not os.path.exists(os.path.join(path, "Images")):
                    os.makedirs(os.path.join(path, "Images"))
                shutil.move(os.path.join(path, file), os.path.join(path, "Images", file))
        print("FILES ORGANIZED")
