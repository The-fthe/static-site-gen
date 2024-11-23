from enum import Enum
from htmlnode import LeafNode
import re


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
            pass
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text,
                            {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "",
                            {"src": text_node.url,
                                "alt": text_node.text
                             })
        case _:
            raise ValueError("Invalid textNode type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"[\!\[\]\(\)]", old_node.text)
        image_sections = extract_markdown_images(old_node.text)
        for i in range(len(sections)):
            image_found = False
            if sections[i] == "":
                continue
            for alt, url in image_sections:
                if sections[i] == alt:
                    image_found = True
                if sections[i] == url:
                    image_found = True
                    split_nodes.append(
                        TextNode(alt, TextType.IMAGE, url)
                    )
                    break
            if image_found is False:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"[\[\]\(\)]", old_node.text)
        link_sections = extract_markdown_links(old_node.text)
        for i in range(len(sections)):
            link_found = False
            if sections[i] == "":
                continue
            for alt, url in link_sections:
                if sections[i] == alt:
                    link_found = True
                if sections[i] == url:
                    link_found = True
                    split_nodes.append(
                        TextNode(alt, TextType.LINK, url)
                    )
                    break
            if link_found is False:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches
