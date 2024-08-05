from classes import Node, BinaryTree
from functions import lexer, parser, post_order_traversal, eval_step

expressao = "58- -8*(58+31)- -14"
# expressao = "-71 * (-76 * 91 * (10 - 5 - -82) - -79)"
# expressao = "1/24 + 1 - 24 * (2 * 2 * -3)"

tokens = lexer(expressao)
print("Tokens:", tokens)

tree = BinaryTree()
rpn_tokens = tree.reverse_polish(tokens, "+-*/()")
print("Reverse Polish Notation Tokens:", rpn_tokens)

expression_tree = parser(rpn_tokens)
tree.root = expression_tree  # Define a raiz da árvore na instância de BinaryTree
print("Post-Order Traversal Tokens:")
post_order_tokens = post_order_traversal(tree.root)
print(post_order_tokens)

print("Evaluating Tree:")
result = eval_step(tree.root, tree)
print("Result:", result)
print("---------------------")
print("Final Tree:")
tree.print_tree(tree.root)
