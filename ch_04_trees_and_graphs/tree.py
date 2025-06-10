from collections import deque
import unittest


class BTreeNode:
    __slots__ = ('value', 'left', 'right')

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BTree:

    def __init__(self, root=None):
        self.root = root

    def __eq__(self, other):
        return id(self) == id(other) or self.as_list() == other.as_list()

    @classmethod
    def from_list(cls, l):
        btree = cls()

        if not l:
            return btree

        node_list = [BTreeNode(value)
                     if value is not None else None
                     for value in l]
        for pos, node in enumerate(node_list):
            if not node:
                continue
            left_pos = 2 * pos + 1
            right_pos = 2 * pos + 2
            if left_pos < len(node_list):
                node.left = node_list[left_pos]
            if right_pos < len(node_list):
                node.right = node_list[right_pos]

        btree.root = node_list[0]

        return btree

    def as_list(self):
        result = []

        if not self.root:
            return result

        q = deque(((self.root, 0),))

        while q:
            node, pos = q.popleft()
            if pos >= len(result):
                result.extend([None] * (pos - len(result) + 1))
            result[pos] = node.value
            if node.left:
                q.append((node.left, 2 * pos + 1))
            if node.right:
                q.append((node.right, 2 * pos + 2))

        return result


class TestBTreeNode(unittest.TestCase):

    def test_tree_node(self):
        node1 = BTreeNode(1)
        node2 = BTreeNode(2)
        node3 = BTreeNode(3, node1, node2)
        node4 = BTreeNode(4, right=node3)
        node5 = BTreeNode(5, left=node4)

        self.assertEqual(node1.value, 1)
        self.assertIsNone(node1.left)
        self.assertIsNone(node1.right)

        self.assertEqual(node2.value, 2)
        self.assertIsNone(node2.left)
        self.assertIsNone(node2.right)

        self.assertEqual(node3.value, 3)
        self.assertIs(node3.left, node1)
        self.assertIs(node3.right, node2)

        self.assertEqual(node4.value, 4)
        self.assertIsNone(node4.left)
        self.assertIs(node4.right, node3)

        self.assertEqual(node5.value, 5)
        self.assertIs(node5.left, node4)
        self.assertIsNone(node5.right)


class TestBTree(unittest.TestCase):

    def test_init(self):
        btree = BTree()
        self.assertIsNone(btree.root)

        btree = BTree(BTreeNode(1))
        self.assertEqual(btree.root.value, 1)
        self.assertIsNone(btree.root.left)
        self.assertIsNone(btree.root.right)

    def test_as_list(self):
        nodes = [BTreeNode(i) for i in range(15)]

        btree = BTree()
        self.assertEqual(btree.as_list(), [])

        btree.root = nodes[0]
        self.assertEqual(btree.as_list(), [0])

        nodes[0].left = nodes[1]
        self.assertEqual(btree.as_list(), [0, 1])

        nodes[1].left = nodes[3]
        self.assertEqual(btree.as_list(), [0, 1, None, 3])

        nodes[3].right = nodes[8]
        self.assertEqual(btree.as_list(), [0, 1, None, 3, None, None, None, None, 8])

        nodes[1].right = nodes[4]
        self.assertEqual(btree.as_list(), [0, 1, None, 3, 4, None, None, None, 8])

        nodes[4].left = nodes[9]
        self.assertEqual(btree.as_list(), [0, 1, None, 3, 4, None, None, None, 8, 9])

        nodes[0].right = nodes[2]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, None, None, None, 8, 9])

        nodes[2].right = nodes[6]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, None, 6, None, 8, 9])

        nodes[6].left = nodes[13]
        self.assertEqual(
            btree.as_list(), [0, 1, 2, 3, 4, None, 6, None, 8, 9, None, None, None, 13]
        )

        nodes[2].left = nodes[5]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, None, 8, 9, None, None, None, 13])

        nodes[5].left = nodes[11]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, None, 8, 9, None, 11, None, 13])

        nodes[4].right = nodes[10]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, None, 8, 9, 10, 11, None, 13])

        nodes[6].right = nodes[14]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, None, 8, 9, 10, 11, None, 13, 14])

        nodes[5].right = nodes[12]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, None, 8, 9, 10, 11, 12, 13, 14])

        nodes[3].left = nodes[7]
        self.assertEqual(btree.as_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_from_list(self):
        # TODO: test incorrect trees
        lists = [
            [],
            [0],
            [0, 1],
            [0, None, 2],
            [0, 1, 2],
            [0, 1, None, 3],
            [0, 1, None, None, 4],
            [0, 1, None, 3, 4],
            [0, None, 2, None, None, 5],
            [0, None, 2, None, None, None, 6],
            [0, None, 2, None, None, 5, 6],
            [0, 1, 2, 3],
            [0, 1, 2, None, 4],
            [0, 1, 2, None, None, 5],
            [0, 1, 2, None, None, None, 6],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, None, 5],
            [0, 1, 2, 3, None, None, 6],
            [0, 1, 2, None, 4, 5],
            [0, 1, 2, None, 4, None, 6],
            [0, 1, 2, None, None, 5, 6],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, None, 6],
            [0, 1, 2, 3, None, 5, 6],
            [0, 1, 2, None, 4, 5, 6],
            [0, 1, 2, 3, 4, 5, 6],
            [0, 1, None, 3, None, None, None, 7],
            [0, 1, None, None, 4, None, None, None, None, 9, 10],
            [0, None, 2, None, None, None, 6, None, None, None, None, None, None, None, 14],
            [0, None, 2, None, None, 5, None, None, None, None, None, None, 12],
            [0, 1, 2, None, None, 5, 6, None, None, None, None, 11, 12],
            [0, 1, 2, 3, 4, 5, None, None, None, None, 10],
            [0, 1, 2, 3, None, None, 6, 7, None, None, None, None, None, None, 14],
            [0, 1, 2, None, 4, 5, None, None, None, 9, None, None, 12],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        ]
        for l in lists:
            btree = BTree.from_list(l)
            self.assertEqual(btree.as_list(), l)

    def test_equality(self):
        lists = [
            [],
            [0],
            [0, None, 2],
            [0, 1, 2],
            [0, None, 2, None, None, 5, 6],
            [0, 1, 2, 3, 4, 5, 6],
            [0, 1, None, None, 4, None, None, None, None, 9, 10],
            [0, 1, 2, None, None, 5, 6, None, None, None, None, 11, 12],
            [0, 1, 2, 3, None, None, 6, 7, None, None, None, None, None, None, 14],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        ]
        for l1 in lists:
            btree1 = BTree.from_list(l1)
            self.assertEqual(btree1, btree1)
            for l2 in lists:
                btree2 = BTree.from_list(l2)
                if l1 == l2:
                    self.assertEqual(btree1, btree2)
                else:
                    self.assertNotEqual(btree1, btree2)
