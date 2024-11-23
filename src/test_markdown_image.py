import unittest

from textnode import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    TextType,
    TextNode

)


class TestMarkdownImage(unittest.TestCase):

    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        check = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                 ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), check)

    def test_markdown_url(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        check = [("to boot dev", "https://www.boot.dev"),
                 ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), check)

    def test_markdown_url2(self):
        text = "This is text with a link [to boot dev1](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        check = [("to boot dev1", "https://www.boot.dev"),
                 ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), check)

    def test_markdown_link_split(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        check = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, check)

    def test_markdown_image_split(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        check = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, check)

    if __name__ == "__main__":
        unittest.main()
