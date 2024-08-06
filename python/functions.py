from classes import Node


def lexer(expression: str) -> list[str]:
    """
    Tokenize the input mathematical expression into operators and operands.

    :param expression: A string containing the mathematical expression.
    :return: A list of tokens (operators and operands).
    """
    valid_ops = ["+", "-", "*", "/", "(", ")"]
    tokens = []
    num: str = ""

    for c in expression:
        if c.isdigit() or c == "-":
            num += c
        else:
            if num:
                tokens.append(num)
                num = ""
            if c in valid_ops:
                tokens.append(c)

    if num:
        tokens.append(num)

    return tokens


precedence = {"*": 1, "/": 1, "+": 0, "-": 0}


def is_number(string: str) -> bool:
    """
    Check if a string is a number.

    :param string: The string to check.
    :return: True if the string represents a number, False otherwise.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def reverse_polish(tokens: list[str]) -> list[str]:
    """
    Convert infix expression tokens to Reverse Polish Notation (RPN).

    :param tokens: A list of tokens from the infix expression.
    :return: A list of tokens in Reverse Polish Notation.
    """
    stack = []
    queue = []

    for token in tokens:
        if is_number(token):
            queue.append(token)
        elif token in precedence:
            while (
                stack
                and stack[-1] in precedence
                and precedence[stack[-1]] >= precedence[token]
            ):
                queue.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()  # Remove the "(" from the stack

    while stack:
        queue.append(stack.pop())

    return queue


def parser(tokens: list[str]) -> Node:
    """
    Parse tokens in Reverse Polish Notation into an expression tree.

    :param tokens: A list of tokens in Reverse Polish Notation.
    :return: The root node of the expression tree.
    """
    stack = []

    for token in tokens:
        if is_number(token):
            stack.append(token)
        else:
            node = Node(token)

            node.right = stack.pop()
            if isinstance(node.right, Node):
                node.right.parent = node

            node.left = stack.pop()
            if isinstance(node.left, Node):
                node.left.parent = node

            stack.append(node)

    return stack.pop()


def eval_tree(root: Node) -> str:
    """
    Evaluate the expression tree.

    :param root: The root node of the expression tree.
    :return: The result of the evaluated expression.
    """
    print(root)

    while not root.is_leaf():
        root.eval_step()
        print(root)

    result = root.eval_leaf()
    print(result)
    return result


def eval_exp(exp_str: str) -> str:
    """
    Evaluate a mathematical expression given as a string.

    :param exp_str: The mathematical expression as a string.
    :return: The result of the evaluated expression as a string.
    """
    tokens = lexer(exp_str)
    rev_pol = reverse_polish(tokens)
    tree_root = parser(rev_pol)

    result = eval_tree(tree_root)
    return result
