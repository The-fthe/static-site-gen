import os
import shutil
import page_generator as pg

from copystatic import copy_files_recursive

dir_path_static = './static'
dir_path_public = './public'
dir_path_content = "./content"


def main():
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copy static files to public directory")
    copy_files_recursive(dir_path_static, dir_path_public)

    pg.generate_pages_recursive(
        dir_path_content,
        os.path.join(dir_path_static, "template.html"),
        dir_path_public
    )


if __name__ == "__main__":
    main()
