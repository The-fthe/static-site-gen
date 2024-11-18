import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
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
