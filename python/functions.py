from classes import Node


def lexer(expressao: str):
    valid_ops = ["+", "-", "*", "/", "(", ")"]
    tokens = []
    num: str = ""

    for c in expressao:
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


def is_number(string):
    try:
        int(string)
        return True
    except ValueError as e:
        return False


def reverse_polish(tokens):
    stack = []
    queue = []

    for token in tokens:
        if is_number(token):
            queue.append(token)
            continue

        if token in precedence.keys():
            while (
                stack
                and stack[-1] in precedence.keys()
                and precedence[stack[-1]] >= precedence[token]
            ):
                queue.append(stack.pop())
            stack.append(token)
            continue

        if token == "(":
            stack.append(token)
            continue

        if token == ")":
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
            continue

    while stack:
        queue.append(stack.pop())

    return queue


def parser(tokens):
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


def eval_tree(root):
    print(root)

    while not root.is_leaf():
        root.eval_step()
        print(root)

    res = root.eval_leaf()
    print(res)
    return res


def eval_exp(exp_str):
    tokens = lexer(exp_str)
    rev_pol = reverse_polish(tokens)
    tree_root = parser(rev_pol)

    res = eval_tree(tree_root)
    return res
