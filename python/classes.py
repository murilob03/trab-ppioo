class Node:
    def __init__(self, token: str):
        """
        Initialize a tree node.

        :param token: The token or operator for this node, e.g., "+", "-", "*", "/".
        """
        self.parent: Node | None = None
        self.left: Node | None | str = None
        self.right: Node | None | str = None
        self.token: str = token

    def is_leaf(self) -> bool:
        """
        Check if the current node is a leaf node.

        A leaf node is a node that does not have any child nodes (both left and right are not nodes).

        :return: True if the node is a leaf, False otherwise.
        """
        return not isinstance(self.left, Node) and not isinstance(self.right, Node)

    def eval_leaf(self) -> str:
        """
        Evaluate the leaf node.

        This method assumes the node is a leaf and its left and right children are numerical values.
        It evaluates the expression based on the token (operator) and returns the result as a string.

        :return: The result of the operation as a string.
        :raises ValueError: If the node is not a leaf.
        """
        if self.is_leaf():
            # Convert the left and right values to integers
            left_val = int(self.left)  # type: ignore
            right_val = int(self.right)  # type: ignore

            # Perform the operation based on the token
            if self.token == "+":
                return str(left_val + right_val)
            elif self.token == "-":
                return str(left_val - right_val)
            elif self.token == "*":
                return str(left_val * right_val)
            elif self.token == "/":
                return str(int(left_val / right_val))
            else:
                raise ValueError(f"Unsupported operator: {self.token}")
        else:
            raise ValueError("This node is not a leaf node.")

    def eval_step(self):
        """
        Perform one evaluation step by finding the deepest leaf node and updating its parent.

        This method performs a breadth-first search (BFS) to find the deepest leaf node,
        evaluates it, and then updates its parent node with the result.
        """
        # Use BFS to find the deepest leaf node
        queue = [(self, 0)]  # (node, depth)
        bottom_leaf = self
        max_depth = 0

        while queue:
            node, depth = queue.pop(0)  # Dequeue node and depth

            if node.is_leaf() and depth >= max_depth:
                bottom_leaf = node
                max_depth = depth

            # Enqueue children nodes with incremented depth
            if isinstance(node.left, Node):
                queue.append((node.left, depth + 1))  # type: ignore
            if isinstance(node.right, Node):
                queue.append((node.right, depth + 1))  # type: ignore

        # Evaluate the bottom leaf node
        leaf_value = bottom_leaf.eval_leaf()

        # Update the parent node with the evaluated value
        if bottom_leaf.parent:
            if bottom_leaf.parent.left is bottom_leaf:
                bottom_leaf.parent.left = leaf_value
            else:
                bottom_leaf.parent.right = leaf_value

    def __str__(self) -> str:
        """
        Return a string representation of the subtree rooted at this node.

        The representation includes parentheses to indicate the structure of the expression.

        :return: The string representation of the subtree.
        """
        # Recursively build the string for the left and right subtrees
        left_str = str(self.left) if isinstance(self.left, Node) else self.left
        right_str = str(self.right) if isinstance(self.right, Node) else self.right

        # Return the complete expression with parentheses
        return f"({left_str} {self.token} {right_str})"
