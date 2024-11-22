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
    textNodes = []

    for node in old_nodes:
        is_delimiter = False
        text = ""
        for c in node.text:
            if c is not delimiter:
                text += c
                continue

            if c is delimiter and is_delimiter is False:
                textNodes.append(TextNode(text, TextType.TEXT))
                text = ""
                is_delimiter = True
                continue

            if c is delimiter and is_delimiter:
                textNodes.append(TextNode(text, text_type))
                text = ""
                is_delimiter = False
                continue
        if len(text) > 0:
            if is_delimiter:
                textNodes.append(TextNode(text, text_type))
            else:
                textNodes.append(TextNode(text, TextType.TEXT))

        if delimiter in node.text and is_delimiter is not False:
            raise ValueError("delimiter is not close")

    return textNodes
