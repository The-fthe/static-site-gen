from enum import Enum
from htmlnode import (
    LeafNode,
    ParentNode
)
from textnode import (
    TextNode,
    text_node_to_html_node,
    text_to_textnodes,
)


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "CODE"
    QUOTE = "quote"
    UNORDERED_LIST = "unorderer_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        htmlNode = text_to_children(block)
        children.append(htmlNode)
    return ParentNode("div", children)


def text_to_children(text):
    block_type = block_to_block_type(text)
    match block_type:
        # case BlockType.PARAGRAPH:
        #     text_nodes = text_to_textnodes(text)
        #     children = []
        #     for text_node in text_nodes:
        #         children.append(text_node_to_html_node(text_node))
        #     return ParentNode("p", children)
        case BlockType.HEADING:
            heading_count = text.count('#')
            text_nodes = text_to_textnodes(text.replace("#", "").strip())
            children = []
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            return ParentNode(f"h{heading_count}", children)
        case BlockType.CODE:
            text_nodes_code = text_to_textnodes(text.replace('`', "").strip())
            stuffs = []
            for text_node_code in text_nodes_code:
                stuffs.append(text_node_to_html_node(text_node_code))
            pre_node = ParentNode("pre", stuffs)
            return ParentNode("code", [pre_node])
        case BlockType.QUOTE:
            text_nodes = text_to_textnodes(text.lstrip("> "))
            children = []
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            return ParentNode("blockquote", children)
        case BlockType.ORDERED_LIST:
            lines = text.split("\n")
            lists = []
            for i in range(len(lines)):
                text_nodes = text_to_textnodes(
                    lines[i].replace(f"{i+1}. ", "")
                )
                children = []
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))
                lists.append(ParentNode("ol", children))
            return ParentNode("li", lists)
        case BlockType.UNORDERED_LIST:
            lines = text.split("\n")
            lists = []
            for i in range(len(lines)):
                text_nodes = text_to_textnodes(lines[i]
                                               .replace("- ", "")
                                               .replace("* ", "")
                                               )
                children = []
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))
                lists.append(ParentNode("ul", children))
            return ParentNode("li", lists)
        case _:
            pass
