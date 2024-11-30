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
        case BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(text.replace("\n", " "))
            children = []
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            return ParentNode("p", children)
        case BlockType.HEADING:
            heading_count = text.count('#')
            text_nodes = text_to_textnodes(text.replace("#", "").strip())
            children = []
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            return ParentNode(f"h{heading_count}", children)
        case BlockType.CODE:
            if not text.startswith("```") or not text.endswith("```"):
                raise ValueError("Invalid code block")
            text_nodes_code = text_to_textnodes(text[4:-3].strip())
            children = []
            for text_node_code in text_nodes_code:
                children.append(text_node_to_html_node(text_node_code))
            pre_node = ParentNode("code", children)
            return ParentNode("pre", [pre_node])
        case BlockType.QUOTE:
            lines = text.split("\n")
            children = []
            new_lines = []
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("Invalid quote block")
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            text_nodes = text_to_textnodes(content)
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            return ParentNode("blockquote", children)
        case BlockType.ORDERED_LIST:
            lines = text.split("\n")
            lists = []
            for line in lines:
                children = []
                line = line[3:]
                text_nodes = text_to_textnodes(line)
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))

                lists.append(ParentNode("li", children))
            return ParentNode("ol", lists)
        case BlockType.UNORDERED_LIST:
            lines = text.split("\n")
            lists = []
            for i in range(len(lines)):
                lines[i] = lines[i][2:]
                text_nodes = text_to_textnodes(lines[i])
                children = []
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))
                lists.append(ParentNode("li", children))
            return ParentNode("ul", lists)
        case _:
            pass
