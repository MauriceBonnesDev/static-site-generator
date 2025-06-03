import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_two_props(self):
        node2 = HTMLNode("This is a html node")
        node3 = HTMLNode("This is a html node")
        node = HTMLNode("h1", "This is a html node", [node2, node3], {"href": "https://www.boot.dev", "test": 1})
        compare_node = HTMLNode("h1", "This is a html node", [node2, node3], {"href": "https://www.boot.dev", "test": 1})
        self.assertEqual(node.props_to_html(), compare_node.props_to_html())

    def test_uneq_props(self):
        node2 = HTMLNode("This is a html node")
        node3 = HTMLNode("This is a html node")
        node = HTMLNode("h1", "This is a html node", [node2, node3], {"href": "https://www.boot.dev", "test": 1})
        compare_node = HTMLNode("h2", "This is a html node", [node2, node3], {"href": "https://www.boot.dev", "test": 2})
        self.assertNotEqual(node.props_to_html(), compare_node.props_to_html())

    def test_uneq_props(self):
        node2 = HTMLNode("This is a html node")
        node3 = HTMLNode("This is a html node")
        node = HTMLNode("h1", "This is a html node", [node2, node3], {"href": "https://www.boot.dev", "test": 1})
        compare_node = HTMLNode("h2", "This is a html node", [node2, node3], {"href": "https://www.boot.com", "test": 1})
        self.assertNotEqual(node.props_to_html(), compare_node.props_to_html())

    def test_eq_one_prop(self):
        node2 = HTMLNode("This is a html node")
        node3 = HTMLNode("This is a html node")
        node = HTMLNode("h1", "This is a html node", [node2, node3], {"href": "https://www.boot.dev"})
        compare_node = HTMLNode("h2", "This is a html node", [node2, node3], {"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), compare_node.props_to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "text 1")
        grandchild_node_1 = LeafNode("i", "text 2")
        grandchild_node_2 = LeafNode("img", "image.png", props={"href": "realimage.png"})
        child_node = ParentNode("span", [grandchild_node, grandchild_node_1, grandchild_node_2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>text 1</b><i>text 2</i><img href="realimage.png">image.png</img></span></div>',
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!", {"font-weight": "bold", "font-size": 14})
        self.assertEqual(node.to_html(), '<h1 font-weight="bold" font-size="14">Hello, world!</h1>')

    def test_leaf_to_html_value(self):
        node = LeafNode(None, "Hello, world!", {"font-weight": "bold", "font-size": 14})
        self.assertEqual(node.to_html(), 'Hello, world!')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("h2", None, {"font-weight": "bold", "font-size": 14})
        with self.assertRaises(ValueError):
           node.to_html()
if __name__ == "__main__":
    unittest.main()
