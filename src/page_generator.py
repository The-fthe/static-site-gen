import os
import extract_title as ex

from blocks import (
    markdown_to_html_node
)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path,
                          dest_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(content_path, template_path, dest_path)
    pass


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
            raise ValueError("Template is em.pty")
        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        with open(dest_path, "w") as file:
            file.write(template)


def main():
    path_markdown = '../content/index.md'
    path_template = '../static/template.html'
    path_static = '../static'
    path_public = '../public'
    path_content = '../content'

    generate_pages_recursive(path_content, path_template, path_public)
    # generate_page(path_markdown, path_template, path_public)


# main()
