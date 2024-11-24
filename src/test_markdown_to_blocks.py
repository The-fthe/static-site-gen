import unittest

from textnode import (
    TextNode,
    TextType,
    text_to_textnodes,
    markdown_to_blocks
)


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

    if __name__ == "__main__":
        unittest.main()
