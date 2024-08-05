use crate::shunt_yard::is_number;
use crate::shunt_yard::shunt_yard;

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

    pub fn evaluate(&self) -> i64 {
        let mut tree_str = self.to_string();
        println!("{}", tree_str);
        self.root.evaluate(&mut tree_str)
    }

    pub fn to_string(&self) -> String {
        self.root.to_string()
    }
}

impl Node {
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

pub fn parser(tokens: Vec<String>) -> Tree {
    let tokens_postfix = shunt_yard(tokens);

    Tree::parse_from_vector(tokens_postfix)
}
