use crate::shunt_yard::is_number;

enum Node {
    String(String),
    Operation {
        operator: String,
        left: Box<Node>,
        right: Box<Node>,
    },
}

pub struct Tree {
    root: Node,
}

impl Tree {
    pub fn parse_from_vector(tokens: Vec<String>) -> Tree {
        let mut stack: Vec<Node> = vec![];

        for token in tokens {
            if is_number(&token) {
                stack.push(Node::String(token));
            } else {
                let op2 = stack.pop().expect("");
                let op1 = stack.pop().expect("");

                let operation = Node::Operation {
                    operator: token,
                    left: Box::new(op1),
                    right: Box::new(op2),
                };

                stack.push(operation);
            }
        }

        let root = stack.pop().expect("Missing root");
        Tree { root }
    }

    pub fn evaluate(&self) -> f64 {
        self.root.evaluate()
    }
}

impl Node {
    fn evaluate(&self) -> f64 {
        match self {
            Node::String(value) => value.parse().expect("Invalid number"),
            Node::Operation {
                operator,
                left,
                right,
            } => {
                let left_val = left.evaluate();
                let right_val = right.evaluate();
                match operator.as_str() {
                    "+" => {
                        println!("{} + {}", left_val, right_val);
                        left_val + right_val
                    }
                    "-" => {
                        println!("{} - {}", left_val, right_val);
                        left_val - right_val
                    }
                    "*" => {
                        println!("{} * {}", left_val, right_val);
                        left_val * right_val
                    }
                    "/" => {
                        println!("{} / {}", left_val, right_val);
                        left_val / right_val
                    }
                    _ => panic!("Unknowm operator!"),
                }
            }
        }
    }
}
