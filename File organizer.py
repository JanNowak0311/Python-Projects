import os
import shutil
print("To exit the app just type in 'out'")
while True:
    path = input("Type in your folder path (e.g. 'your/folder/path')")
    if path == "out":
        print("Goodbye")
        break
    else:
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
