import unittest

from htmlnode import LeafNode


class TestLeftNode(unittest.TestCase):
    def test_prop_to_tag(self):
        node = LeafNode("h1", None, None)
        check_html = "h1"
        self.assertEqual(node.tag, check_html)

    def test_prop_to_value(self):
        node = LeafNode(None, "this is a good day to die",  None)
        check_html = "this is a good day to die"
        self.assertEqual(node.value, check_html)

    def test_prop_to_html_1_set(self):
        dict = {"href": "https://www.google.com"}
        node = LeafNode("a", "", dict)
        check_html = " href=\"https://www.google.com\""
        self.assertEqual(node.props_to_html(), check_html)

    def test_prop_to_html_2_set(self):
        dict = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("", "",  dict)
        check_html = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), check_html)

    def test_to_html(self):
        dict = {"href": "https://www.google.com"}
        node = LeafNode("a", "Click me!", dict)
        check_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), check_html)

    def test_to_html2(self):
        node = LeafNode("p", "Click me!", None)
        check_html = '<p>Click me!</p>'
        self.assertEqual(node.to_html(), check_html)


if __name__ == "__main__":
    unittest.main()
