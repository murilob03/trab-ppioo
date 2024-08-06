use std::collections::HashMap;

// Helper function to check if a string represents a number.
fn is_number(s: &str) -> bool {
    s.parse::<f64>().is_ok()
}

// Converts an infix expression to postfix notation using the Shunting Yard algorithm.
fn reverse_polish(tokens_infix: Vec<String>) -> Vec<String> {
    // Operator precedence map
    let op_precedence: HashMap<String, u32> = HashMap::from([
        ('*'.to_string(), 1),
        ('/'.to_string(), 1),
        ('+'.to_string(), 0),
        ('-'.to_string(), 0),
    ]);

    // Stack to hold operators and parentheses
    let mut stack: Vec<String> = vec![];
    // Output queue for the postfix expression
    let mut queue: Vec<String> = vec![];

    for token in tokens_infix {
        // If token is a number, add it to the output queue
        if is_number(&token) {
            queue.push(token);
        } else if op_precedence.contains_key(&token) {
            // Process operators
            while let Some(top) = stack.last() {
                if op_precedence.contains_key(top)
                    && op_precedence.get(top) >= op_precedence.get(&token)
                {
                    queue.push(stack.pop().unwrap());
                } else {
                    break;
                }
            }
            stack.push(token);
        } else if token == "(" {
            // Push left parenthesis to the stack
            stack.push(token);
        } else if token == ")" {
            // Pop from stack to queue until left parenthesis is encountered
            while let Some(op) = stack.pop() {
                if op == "(" {
                    break;
                } else {
                    queue.push(op);
                }
            }
        }
    }

    // Pop all remaining operators in the stack to the queue
    while let Some(op) = stack.pop() {
        queue.push(op);
    }

    queue
}

// Enum to represent nodes in the expression tree
enum Node {
    String(String),
    Operation {
        operator: String,
        left: Box<Node>,
        right: Box<Node>,
    },
}

// Structure to represent the expression tree
pub struct Tree {
    root: Node,
}

impl Tree {
    // Constructs a Tree from a vector of tokens in postfix notation
    pub fn parse_from_vector(tokens: Vec<String>) -> Tree {
        let mut stack: Vec<Node> = vec![];

        for token in tokens {
            if is_number(&token) {
                stack.push(Node::String(token));
            } else {
                let right = stack.pop().expect("Missing operand for operator");
                let left = stack.pop().expect("Missing operand for operator");

                let operation = Node::Operation {
                    operator: token,
                    left: Box::new(left),
                    right: Box::new(right),
                };

                stack.push(operation);
            }
        }

        let root = stack.pop().expect("Missing root node");
        Tree { root }
    }

    // Evaluates the expression tree and returns the result
    pub fn evaluate(&self) -> i64 {
        let mut tree_str = self.to_string();
        println!("{}", tree_str);
        self.root.evaluate(&mut tree_str)
    }

    // Converts the expression tree to its string representation
    pub fn to_string(&self) -> String {
        self.root.to_string()
    }
}

impl Node {
    // Evaluates the node and its children, updating the tree_str
    fn evaluate(&self, tree_str: &mut String) -> i64 {
        match self {
            Node::String(value) => value.parse().expect("Invalid number"),
            Node::Operation {
                operator,
                left,
                right,
            } => {
                let left_val = left.evaluate(tree_str);
                let right_val = right.evaluate(tree_str);
                let op_str = format!(
                    "({} {} {})",
                    left_val.to_string(),
                    operator,
                    right_val.to_string()
                );
                let result = match operator.as_str() {
                    "+" => left_val + right_val,
                    "-" => left_val - right_val,
                    "*" => left_val * right_val,
                    "/" => left_val / right_val,
                    _ => panic!("Unknown operator!"),
                };

                *tree_str = tree_str.replace(&op_str, &result.to_string());
                println!("{}", tree_str);

                result
            }
        }
    }

    // Converts the node to its string representation
    fn to_string(&self) -> String {
        match self {
            Node::String(value) => value.clone(),
            Node::Operation {
                operator,
                left,
                right,
                ..
            } => {
                let left_expr = left.to_string();
                let right_expr = right.to_string();
                format!("({} {} {})", left_expr, operator, right_expr)
            }
        }
    }
}

// Parses a vector of infix tokens into a Tree
pub fn parser(tokens: Vec<String>) -> Tree {
    let tokens_postfix = reverse_polish(tokens);
    Tree::parse_from_vector(tokens_postfix)
}
