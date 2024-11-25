from enum import Enum


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
    if len(block) > 2:
        # check for header
        if block[0] == '#' and \
                block.count('#') and \
                block[block.count('#')] == " ":
            return BlockType.HEADING
        # check for code
        if block.count('`') == 6 and \
                block[:3].count('`') == 3 and \
                block[:-3].count('`') == 3:
            return BlockType.CODE
        # check for quote
        if block[0] == '>':
            return BlockType.QUOTE
        # check for unorder list '*'
        if (block[0] == '*' or block[0] == '-') and block[1] == " ":
            return BlockType.UNORDERED_LIST
        # check for order list
        if block[0].isdigit() and block[1] == ".":
            lists = block.split('\n')
            if len(lists) == 1:
                return BlockType.ORDERED_LIST
            for i in range(len(lists)):
                if lists[i][0].isdigit() is False or lists[i][1] != ".":
                    return BlockType.PARAGRAPH
                if i == 0:
                    continue
                if int(lists[i-1][0])+1 != int(lists[i][0]) or lists[i][1] != ".":
                    return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
