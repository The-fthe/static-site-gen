import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_prop_to_tag(self):
        node = HTMLNode("h1", None, None, None)
        check_html = "h1"
        self.assertEqual(node.tag, check_html)

    def test_prop_to_value(self):
        node = HTMLNode(None, "this is a good day to die", None, None)
        check_html = "this is a good day to die"
        self.assertEqual(node.value, check_html)

    def test_prop_to_child(self):
        htmlNode = HTMLNode("h1", "this is a google")
        node = HTMLNode("h1", "this is a google", htmlNode)
        self.assertEqual(node.children, htmlNode)

    def test_prop_to_html_1_set(self):
        dict = {"href": "https://www.google.com"}
        node = HTMLNode("", "", None, dict)
        check_html = "href=\"https://www.google.com\""
        self.assertEqual(node.props_to_html(), check_html)

    def test_prop_to_html_2_set(self):
        dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("", "", None, dict)
        check_html = "href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), check_html)

    def test_prop_to_html_0_set(self):
        dict = {}
        node = HTMLNode("", "", None, dict)
        check_html = ""
        self.assertEqual(node.props_to_html(), check_html)


if __name__ == "__main__":
    unittest.main()
