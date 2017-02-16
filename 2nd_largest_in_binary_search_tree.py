class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __repr__(self):
        return "<%s>" % (self.value) 


def find_largest(head):

    if not head:
        raise Exception("Tree must have at least 1 node")

    current = head

    while current.right:
        current = current.right

    return current.value


def find_2nd_largest(head):

    if not head or (not head.right and not head.left):
        raise Exception("Tree must have at least 2 nodes")

    if head.left and not head.right:
        return find_largest(head.left)

    if head.right and (not head.right.left and not head.right.right):
        return head.value

    return find_2nd_largest(head.right)


def find_2nd_largest_iter(head):

    if not head or (not head.right and not head.left):
        raise Exception("Tree must have at least 2 nodes")

    current = head
    parent = None

    while current.right:
        parent = curent
        current = current.right

    if current.left:
        return find_largest(current.left)
    else:
        return parent


def find_2nd_largest_recur(tree):

    if tree.right:
        return find_2nd_largest_recur(tree.right)

    return tree.value


a = BinaryTreeNode(3)
b = BinaryTreeNode(2)
c = BinaryTreeNode(5)
d = BinaryTreeNode(1)
e = BinaryTreeNode(4)

a.left = b
a.right = c
b.left = d
c.left = e