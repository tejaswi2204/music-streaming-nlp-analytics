import os

def print_tree(start_path, prefix=""):
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
        return

    for i, item in enumerate(items):
        path = os.path.join(start_path, item)
        is_last = i == len(items) - 1

        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_tree(path, prefix + extension)

# Your folder path
folder_path = r"C:\Users\User\Downloads\Analysis on Music streaming platforms"

print(folder_path)
print_tree(folder_path)