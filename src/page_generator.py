import os
import extract_title as ex

from blocks import (
    markdown_to_html_node
)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    title = None
    content = None

    with open(from_path, 'r') as file:
        markdown = file.read()
        title = ex.extract_title(markdown)
        content = markdown_to_html_node(markdown).to_html()
        # print(f"content: \n{content}")
    with open(template_path, 'r') as file:
        template = file.read() \
            .replace('{{ Title }}', title) \
            .replace('{{ Content }}', content)

        if template is None:
            raise ValueError("Template is empty")
        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        with open(dest_path, "w") as file:
            file.write(template)


def main():
    path_markdown = '../static/content/index.md'
    path_template = '../static/template.html'
    path_public = '../public/index.html'
    generate_page(path_markdown, path_template, path_public)


# main()
