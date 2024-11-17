import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
