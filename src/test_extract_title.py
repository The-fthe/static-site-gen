import unittest
import extract_title as ex


class TestExtractTitle(unittest.TestCase):
    def test_header_extraction(self):
        markdown = "# this is a header1\n this is nothing text"
        check_value = "this is a header1"

        self.assertEqual(ex.extract_title(markdown), check_value)

    def test_header_not_available(self):
        markdown = "## this is a header1\n this is nothing text"
        with self.assertRaises(ValueError) as context:
            ex.extract_title(markdown)
        self.assertEqual(str(context.exception), "Header is not provided")

    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(ValueError) as context:
            ex.extract_title(markdown)
        self.assertEqual(str(context.exception), "Empty markdown!!")

    def test_eq(self):
        actual = ex.extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = ex.extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = ex.extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            ex.extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
