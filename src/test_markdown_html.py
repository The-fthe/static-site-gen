import unittest

from blocks import (
    markdown_to_html_node
)


class TestMarkdownToHTML(unittest.TestCase):
    # def test_paragraph_html(self):
    #     markdown = "hello world"
    #     html = '<div><p>hello world</p></div>'
    #     result = markdown_to_html_node(markdown).to_html()
    #     self.assertEqual(result, html)

    def test_heading_html(self):
        markdown = "#### This is a quote"
        html = '<div><h4>This is a quote</h4></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_quote_html(self):
        markdown = ">This is a quote"
        html = '<div><blockquote>This is a quote</blockquote></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_code_html(self):
        markdown = "```\nThis is a code\ncoding\n```"
        html = '<div><pre><code>This is a code\ncoding</code></pre></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_unorder_list_html(self):
        markdown = "- This is a list\n- This is a list2\n- This is a list3"
        html = '<div><ul><li>This is a list</li><li>This is a list2</li><li>This is a list3</li></ul></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_unorder_list_2_html(self):
        markdown = "* This is a list\n* This is a list2\n* This is a list3"
        html = '<div><ul><li>This is a list</li><li>This is a list2</li><li>This is a list3</li></ul></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_order_list__html(self):
        markdown = "1. This is a list\n2. This is a list2\n3. This is a list3"
        html = '<div><ol><li>This is a list</li><li>This is a list2</li><li>This is a list3</li></ol></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_heading_quote_html(self):
        markdown = "### This is a header\n\n>This is a quote\n\n#### This is second header"
        html = '<div><h3>This is a header</h3><blockquote>This is a quote</blockquote><h4>This is second header</h4></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_heading_code_html(self):
        markdown = "### This is a header\n\n```\nThis is a code\nThis is a code2\n```\n\n#### This is second header"
        html = '<div><h3>This is a header</h3><pre><code>This is a code\nThis is a code2</code></pre><h4>This is second header</h4></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items


1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
