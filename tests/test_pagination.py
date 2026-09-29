import unittest

from pagination import has_next_page


class PaginationTests(unittest.TestCase):
    def test_partial_result_has_next_page(self):
        self.assertTrue(has_next_page(21, 0, 10))

    def test_exact_last_page_has_no_next_page(self):
        self.assertFalse(has_next_page(20, 10, 10))

    def test_empty_collection_has_no_next_page(self):
        self.assertFalse(has_next_page(0, 0, 10))

    def test_invalid_page_size_is_rejected(self):
        with self.assertRaises(ValueError):
            has_next_page(20, 0, 0)


if __name__ == "__main__":
    unittest.main()
