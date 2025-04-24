import os
import shutil
import mimetypes

MIME_TYPE_CATEGORIES = {
    "image": "Images",
    "video": "Videos",
    "audio": "Audio",
    "text": "Documents",
    "application": "Documents",
}

print("To exit the app just type in 'out'")
while True:
    path = input("Type in your folder path (e.g. 'your/folder/path') ")
    if path == "out":
        print("Goodbye")
        break
    else:
        if not os.path.isdir(path):
            print("Invalid path. Please enter a valid folder path.")
            continue
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path) or file.startswith("."):
                continue
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                category = "Others"
            else:
                main_type = mime_type.split("/")[0]
                category = MIME_TYPE_CATEGORIES.get(main_type, "Others")
            category_path = os.path.join(path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            shutil.move(file_path, os.path.join(category_path, file))

        print("FILES ORGANIZED")
