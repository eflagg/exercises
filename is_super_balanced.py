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

    def is_super_balanced(self, node):
        """Return false if difference of depths between any two leaf nodes is 
        greater than 1; otherwise return true"""

        if not node:
            return True

        min_depth = None
        max_depth = None

        to_visit = [(node, 0)]

        while to_visit:
            current_node, curent_depth = to_visit.pop()
            if not current_node.left and not current_node.right:
                min_depth = min(min_depth, current_depth)
                max_depth = max(max_depth, current_depth)
                if max_depth - min_depth > 1:
                    return False
            if current_node.left:
                to_visit.append((current_node.left, current_depth + 1))
            if current_node.right:
                to_visit.append(current_node.right, current_depth + 1))
        
        return True

