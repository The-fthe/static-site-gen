import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_prop_to_tag(self):
        children = [
            LeafNode("b", "Bold text"),
        ]
        node = ParentNode("h1", children, "test")
        check_html = "h1"
        self.assertEqual(node.tag, check_html)

    def test_chidlren_1(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", children)
        check_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), check_html)

    def test_chidlren_2(self):
        dict = {"href": "https://www.google.com"}
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("a", "italic text", dict),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", children)
        check_html = '<p><b>Bold text</b>Normal text<a href="https://www.google.com">italic text</a>Normal text</p>'
        self.assertEqual(node.to_html(), check_html)

    def test_chidlren_3(self):
        dict = {"href": "https://www.google.com"}
        children = [
            LeafNode("b", "Bold text"),
            LeafNode("a", "italic text", dict),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", children)
        check_html = '<p><b>Bold text</b><a href="https://www.google.com">italic text</a>Normal text</p>'
        self.assertEqual(node.to_html(), check_html)

    def test_chidlren_4(self):
        dict = {"href": "https://www.google.com"}
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", children, dict)
        check_html = '<p href="https://www.google.com"><b>Bold text</b>Normal text</p>'
        self.assertEqual(node.to_html(), check_html)


if __name__ == "__main__":
    unittest.main()
