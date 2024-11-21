import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node",
                        TextType.BOLD,
                        "www.github.The-fthe.com"
                        )
        node2 = TextNode("This is a text node",
                         TextType.BOLD,
                         "www.github.The-fthe.com"
                         )
        self.assertEqual(node, node2)

    def test_eq_enum(self):
        node = TextNode("",
                        TextType.BOLD
                        )
        node2 = TextNode("",
                         TextType.BOLD
                         )
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("",
                        TextType.BOLD,
                        None
                        )
        node2 = TextNode("",
                         TextType.BOLD,
                         None
                         )
        self.assertEqual(node, node2)

    def test_eq_url_repr(self):
        node = TextNode("",
                        TextType.BOLD,
                        None
                        )
        node2 = TextNode("",
                         TextType.BOLD,
                         None
                         )
        self.assertEqual(f"{node}", f"{node2}")

    def test_text_text_not_equal(self):
        node = TextNode("",
                        TextType.ITALIC,
                        None
                        )
        node2 = TextNode("",
                         TextType.BOLD,
                         None
                         )
        self.assertNotEqual(f"{node}", f"{node2}")

    def test_text_not_equal(self):
        node = TextNode("this is not equal",
                        TextType.ITALIC,
                        None
                        )
        node2 = TextNode(" I am find thanks",
                         TextType.ITALIC,
                         None
                         )
        self.assertNotEqual(node, node2)

    def test_url_not_equal(self):
        node = TextNode("this is test",
                        TextType.ITALIC,
                        "www.google.com"
                        )
        node2 = TextNode("this is test",
                         TextType.ITALIC,
                         "www.gogle.com"
                         )
        self.assertNotEqual(node, node2)

    def test_textnode_to_html_type_text(self):
        node2 = TextNode("this is a test",
                         TextType.TEXT,
                         None
                         )
        check_html = 'this is a test'
        self.assertEqual(node2.text_node_to_html_node().to_html(), check_html)

    def test_textnode_to_html_type_text(self):
        node2 = TextNode("this is a test",
                         TextType.TEXT,
                         None
                         )
        check_html = 'this is a test'
        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)

    def test_textnode_to_html_type_bold(self):
        node2 = TextNode("this is a test",
                         TextType.BOLD,
                         None
                         )
        check_html = '<b>this is a test</b>'
        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)

    def test_textnode_to_html_type_italic(self):
        node2 = TextNode("this is a test",
                         TextType.ITALIC,
                         None
                         )
        check_html = '<i>this is a test</i>'
        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)

    def test_textnode_to_html_type_code(self):
        node2 = TextNode("this is a test",
                         TextType.CODE,
                         None
                         )
        check_html = '<code>this is a test</code>'
        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)

    def test_textnode_to_html_type_link(self):
        node2 = TextNode("this is a test",
                         TextType.LINK,
                         "www.google.com"
                         )
        check_html = '<a href="www.google.com">this is a test</a>'

        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)

    def test_textnode_to_html_type_img(self):
        node2 = TextNode("this is a image",
                         TextType.IMAGE,
                         "www.google.com"
                         )
        check_html = '<img src="www.google.com" alt="this is a image"></img>'

        self.assertEqual(text_node_to_html_node(node2).to_html(), check_html)


if __name__ == "__main__":
    unittest.main()
