import unittest

from textnode import (
    TextNode,
    TextType
)

from blocks import (markdown_to_blocks, BlockType, block_to_block_type)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_1(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        check_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]

        new_blocks = markdown_to_blocks(text)
        for i in range(len(check_blocks)):
            self.assertEqual(new_blocks[i], check_blocks[i])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_block_types(self):
        blocks = [
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "## This is **bolded** paragraph",
            "``` This is a code block\n```",
            ">This is **bolded** quote",
            "* This is a unorder list1\n* with items",
            "- This is a unorder list2\n- with items",
            "1. This is a order list\n2. with items",
        ]
        checks = [
            BlockType.PARAGRAPH,
            BlockType.HEADING,
            BlockType.CODE,
            BlockType.QUOTE,
            BlockType.UNORDERED_LIST,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST,
        ]
        for i in range(len(blocks)):
            self.assertEqual(block_to_block_type(
                blocks[i]), checks[i], f"index: {i} is not equal")

    def test_markdown_to_block_type_paragraph(self):
        blocks = [
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "#This is **bolded** paragraph",
            "`` This is a code block```",
            "<This is **bolded** quote",
            "*This is a unorder list1\n* with items",
            "-This is a unorder list2\n* with items",
            "1.This is a order list\n3. with items",
            "2.This is a order list\n1. with items",
            "1.This is a order list\n1. with items",
        ]
        checks = [
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
        ]
        for i in range(len(blocks)):
            self.assertEqual(block_to_block_type(
                blocks[i]), checks[i], f"index:{i} is not equal")

    def test_markdown_to_block_type_orderlist(self):
        blocks = [
            "1. This is a order list\n2. with items\n3. with more item",
            "1. This is a order list",
            "1. This is a order list\n2.  with items",
            "1. This is a order list\n2. with items",
        ]
        checks = [
            BlockType.ORDERED_LIST,
            BlockType.ORDERED_LIST,
            BlockType.ORDERED_LIST,
            BlockType.ORDERED_LIST,
        ]
        for i in range(len(blocks)):
            self.assertEqual(block_to_block_type(
                blocks[i]), checks[i], f"index:{i} is not equal")
    if __name__ == "__main__":
        unittest.main()
