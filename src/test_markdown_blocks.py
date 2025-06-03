import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_html_node

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_for_h3(self):
        block = "###Test Heading 3"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_for_code(self):
        block = """
```
This is a code block
```
"""
        block_type = block_to_block_type(block.strip())

        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_for_quote(self):
        block = ">Test Quote"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_for_ul(self):
        block = """
- first item
- second item
- third item
"""
        block_type = block_to_block_type(block.strip())

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_for_ol(self):
        block = """
1. first item
2. second item
3. third item
"""
        block_type = block_to_block_type(block.strip())

        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_headings(self):
        md = """
### This is a heading 3

## This is a heading 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a heading 3</h3><h2>This is a heading 2</h2></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = """
1. First Item
2. Second Item
3. Third Item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First Item</li><li>Second Item</li><li>Third Item</li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
- First Item
- Second Item
- Third Item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First Item</li><li>Second Item</li><li>Third Item</li></ul></div>",
        )

if "__name__" == "__main__":
    unittest.main()
