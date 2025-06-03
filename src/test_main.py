import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)
        """
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

if "__name__" == "__main__":
    unittest.main()
