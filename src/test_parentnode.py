import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_prop_to_tag(self):
        node = ParentNode("h1", None, None)
        check_html = "h1"
        self.assertEqual(node.tag, check_html)

    def test_prop_to_value(self):
        node = ParentNode(None, "this is a good day to die",  None)
        check_html = "this is a good day to die"
        self.assertEqual(node.value, check_html)

    def test_chidlren_1(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", "", children)
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

        node = ParentNode("p", "", children)
        check_html = '<p><b>Bold text</b>Normal text<a href="https://www.google.com">italic text</a>Normal text</p>'
        self.assertEqual(node.to_html(), check_html)

    def test_chidlren_3(self):
        dict = {"href": "https://www.google.com"}
        children = [
            LeafNode("b", "Bold text"),
            LeafNode("a", "italic text", dict),
            LeafNode(None, "Normal text"),
        ]

        node = ParentNode("p", "", children)
        check_html = '<p><b>Bold text</b><a href="https://www.google.com">italic text</a>Normal text</p>'
        self.assertEqual(node.to_html(), check_html)


if __name__ == "__main__":
    unittest.main()
