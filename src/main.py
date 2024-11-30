from textnode import TextNode, TextType
from os import (
    path,
    mkdir,
    listdir
)
from shutil import (
    copy
)


def get_paths(root, file_paths):
    files = listdir(root)
    for file in files:
        if "." in file:
            file_path = path.join(root, file)
            file_paths.append(file_path)
        elif "." not in file:
            get_paths(path.join(root, file), file_paths)

    if "." not in files and len(root) > 0:
        return file_paths


def get_dirs(root, file_dirs):
    files = listdir(root)
    for file in files:
        if "." not in file:
            file_dir = path.join(root, file)
            file_dirs.append(file_dir)
            get_dirs(path.join(root, file), file_dirs)

    if "." not in files and len(root) > 0:
        return


def main():
    public_path = path.join('.', 'public')
    public_image_path = path.join(public_path, 'images')

    static_path = path.join(".", "static")

    # check public path if not available create one
    if not path.exists(public_path):
        mkdir(public_path)

    # get static paths
    static_files = []
    get_paths(static_path, static_files)
    print(f"static files:\n{static_files}")

    # get  static dir
    static_dirs = []
    get_dirs(static_path, static_dirs)
    print(f"static dirs:\n{static_dirs}")

    # set public path
    public_files = []
    for static_file in static_files:
        file = static_file[len(static_path)+1:]
        public_files.append(path.join(public_path, file))

    print(f"public files:\n{public_files}")

    # set and create public dir
    public_dirs = []
    for static_dirs in static_dirs:
        file = static_dirs[len(static_path)+1:]
        public_dir = path.join(public_path, file)
        public_dirs.append(public_dir)
        if not path.exists(public_dir):
            mkdir(public_dir)
    print(f"public dirs:\n{public_dirs}")

    for i in range(len(static_files)):
        copy(static_files[i], public_files[i])

    print(f'public files:\n{listdir(public_path)}')


if __name__ == "__main__":
    main()
