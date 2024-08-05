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

    def print_tree(self, node, level=0, label="."):
        prefix = " " * (level * 4)
        print(prefix + label + ": " + str(node.token))
        if node.left:
            self.print_tree(node.left, level + 1, "L")
        if node.right:
            self.print_tree(node.right, level + 1, "R")
