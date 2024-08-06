class Node:
    def __init__(self, token):
        self.parent: Node | None = None
        self.left: Node | None | str = None
        self.right: Node | None | str = None
        self.token: str = token

    def is_leaf(self):
        return not isinstance(self.left, Node) and not isinstance(self.right, Node)

    def eval_leaf(self):
        if self.is_leaf():
            left_val = int(self.left)  # type: ignore
            right_val = int(self.right)  # type: ignore
            if self.token == "+":
                return str(left_val + right_val)
            elif self.token == "-":
                return str(left_val - right_val)
            elif self.token == "*":
                return str(left_val * right_val)
            elif self.token == "/":
                return str(int(left_val / right_val))
        else:
            raise ValueError("This node is not a leaf node.")

    def eval_step(self):
        # Use BFS or DFS to find the bottom leaf
        stack = [(self, 0)]
        bottom_leaf = self
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node.is_leaf() and depth >= max_depth:
                bottom_leaf = node
                max_depth = depth
            if isinstance(node.left, Node):
                stack.append((node.left, depth + 1))  # type: ignore
            if isinstance(node.right, Node):
                stack.append((node.right, depth + 1))  # type: ignore

        # Evaluate the bottom leaf node
        leaf_value = bottom_leaf.eval_leaf()

        # Update the parent node
        if bottom_leaf.parent:  # verify if self is not the root
            if bottom_leaf.parent.left is bottom_leaf:
                bottom_leaf.parent.left = leaf_value
            else:
                bottom_leaf.parent.right = leaf_value

    def __str__(self):
        # Monta a string da sub-árvore esquerda
        left_str = str(self.left)

        # Monta a string da sub-árvore direita
        right_str = str(self.right)

        # Retorna a expressão completa com parênteses
        return f"({left_str} {self.token} {right_str})"
