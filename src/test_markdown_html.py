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
        html = '<div><code><pre>This is a code\ncoding</pre></code></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_unorder_list_html(self):
        markdown = "- This is a list\n- This is a list2\n- This is a list3"
        html = '<div><li><ul>This is a list</ul><ul>This is a list2</ul><ul>This is a list3</ul></li></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_unorder_list_2_html(self):
        markdown = "* This is a list\n* This is a list2\n* This is a list3"
        html = '<div><li><ul>This is a list</ul><ul>This is a list2</ul><ul>This is a list3</ul></li></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_order_list__html(self):
        markdown = "1. This is a list\n2. This is a list2\n3. This is a list3"
        html = '<div><li><ol>This is a list</ol><ol>This is a list2</ol><ol>This is a list3</ol></li></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_heading_quote_html(self):
        markdown = "### This is a header\n\n>This is a quote\n\n#### This is second header"
        html = '<div><h3>This is a header</h3><blockquote>This is a quote</blockquote><h4>This is second header</h4></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)

    def test_heading_code_html(self):
        markdown = "### This is a header\n\n```\nThis is a code\nThis is a code2\n```\n\n#### This is second header"
        html = '<div><h3>This is a header</h3><code><pre>This is a code\nThis is a code2</pre></code><h4>This is second header</h4></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, html)


if __name__ == "__main__":
    unittest.main()
