class Node:
    def __init__(self, token):
        self.left = None
        self.right = None
        self.token = token

class BinaryTree:
    def __init__(self):
        self.root = None

    def _get_precedence(self, op):
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 0,
            ')': 0
        }
        return precedence.get(op, -1)

    def reverse_polish(self, tokens, operators):
        queue = []
        operatorStack = []

        for token in tokens:
            if token.lstrip('-').replace('.', '').isdigit():  # Verifica números decimais e negativos
                queue.append(token)
            elif token == '(':
                operatorStack.append(token)
            elif token == ')':
                while operatorStack and operatorStack[-1] != '(':
                    queue.append(operatorStack.pop())
                operatorStack.pop()  # Remove o '(' da pilha
            elif token in operators:
                while (operatorStack and operatorStack[-1] != '(' and
                       self._get_precedence(operatorStack[-1]) >= self._get_precedence(token)):
                    queue.append(operatorStack.pop())
                operatorStack.append(token)
            print("OpStack: " + str(operatorStack))
            print("Queue: " + str(queue))

        while operatorStack:
            queue.append(operatorStack.pop())

        print("Final Queue: " + str(queue))
        return queue

    def parser(self, tokens):
        stack = []

        for token in tokens:
            if token.lstrip('-').replace('.', '').isdigit():  # Verifica números decimais e negativos
                actual_node = Node(token)
                stack.append(actual_node)
            else:
                actual_node = Node(token)
                if len(stack) >= 2:
                    actual_node.right = stack.pop()
                    actual_node.left = stack.pop()
                stack.append(actual_node)

        self.root = stack[0] if stack else None
        return self.root

    def print_tree(self, node, level=0, label="."):
        prefix = " " * (level * 4)
        print(prefix + label + ": " + str(node.token))
        if node.left:
            self.print_tree(node.left, level + 1, "L")
        if node.right:
            self.print_tree(node.right, level + 1, "R")

def lexer(expressao):
    tokens = []
    num = ""
    i = 0
    
    while i < len(expressao):
        char = expressao[i]
        
        if char.isdigit() or (char == '.' and num) or (char == '-' and (not num or num == '(' or num == '+')):
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in '()+-*/':
                tokens.append(char)
        
        i += 1
    
    if num:
        tokens.append(num)
    
    return tokens

def eval_step(node, tree):
    if node is None:
        return 0

    # Se for um nó folha, retorna o valor do token
    if node.left is None and node.right is None:
        return float(node.token)
    
    left_val = eval_step(node.left, tree)
    right_val = eval_step(node.right, tree)
    
    if node.token == '+':
        result = left_val + right_val
    elif node.token == '-':
        result = left_val - right_val
    elif node.token == '*':
        result = left_val * right_val
    elif node.token == '/':
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

if __name__ == "__main__":
    expressao = "1/24 + 1 - 24 * (2 * 2 * -3)"

    tokens = lexer(expressao)
    print("Tokens:", tokens)

    tree = BinaryTree()
    rpn_tokens = tree.reverse_polish(tokens, "+-*/()")
    print("Reverse Polish Notation Tokens:", rpn_tokens)

    expression_tree = tree.parser(rpn_tokens)
    print("Post-Order Traversal Tokens:")
    post_order_tokens = post_order_traversal(tree.root)
    print(post_order_tokens)

    print("Evaluating Tree:")
    result = eval_step(tree.root, tree)
    print("Result:", result)
    print("Final Tree:")
    tree.print_tree(tree.root)
