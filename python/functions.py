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


def parser(tokens):
    stack = []

    for token in tokens:
        if (
            token.lstrip("-").replace(".", "").isdigit()
        ):  # Verifica números decimais e negativos
            actual_node = Node(token)
            stack.append(actual_node)
        else:
            actual_node = Node(token)
            if len(stack) >= 2:
                actual_node.right = stack.pop()
                actual_node.left = stack.pop()
            stack.append(actual_node)

    return stack[0] if stack else None


def eval_step(node, tree):
    if node is None:
        return 0

    # Se for um nó folha, retorna o valor do token
    if node.left is None and node.right is None:
        return float(node.token)

    left_val = eval_step(node.left, tree)
    right_val = eval_step(node.right, tree)

    if node.token == "+":
        result = left_val + right_val
    elif node.token == "-":
        result = left_val - right_val
    elif node.token == "*":
        result = left_val * right_val
    elif node.token == "/":
        result = left_val / right_val
    else:
        raise ValueError(f"Operação desconhecida: {node.token}")

    # Atualiza o token do nó atual com o resultado da operação
    node.token = str(result)

    # Remove os filhos, pois a operação já foi realizada
    node.left = None
    node.right = None

    # Imprime a árvore após a operação
    print("\nÁrvore após realizar a operação:")
    tree.print_tree(tree.root)
    expression_str = tree_to_string(tree.root)
    print("Expression String:", expression_str)

    return result


def post_order_traversal(node):
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.token)

    traverse(node)
    return result


def tree_to_string(node):
    if node is None:
        return ""

    # Se for um nó folha, retorna o valor do token
    if node.left is None and node.right is None:
        return node.token

    # Monta a string da sub-árvore esquerda
    left_str = tree_to_string(node.left)

    # Monta a string da sub-árvore direita
    right_str = tree_to_string(node.right)

    # Retorna a expressão completa com parênteses
    return f"({left_str} {node.token} {right_str})"
