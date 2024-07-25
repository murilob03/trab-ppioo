use std::collections::HashMap;

pub fn is_number(s: &str) -> bool {
    s.parse::<f64>().is_ok()
}

pub fn shunt_yard(tokens_infix: Vec<String>) -> Vec<String> {
    let op_precedence: HashMap<String, u32> = HashMap::from([
        ('*'.to_string(), 1),
        ('/'.to_string(), 1),
        ('+'.to_string(), 0),
        ('-'.to_string(), 0),
    ]);

    let mut stack: Vec<String> = vec![];
    let mut queue: Vec<String> = vec![];

    for token in tokens_infix {
        if is_number(&token) {
            queue.push(token);
            continue;
        }

        if op_precedence.contains_key(&token) {
            while let Some(x) = stack.last() {
                if op_precedence.contains_key(x)
                    && op_precedence.get(x) >= op_precedence.get(&token)
                {
                    queue.push(stack.pop().unwrap());
                } else {
                    break;
                }
            }
            stack.push(token);
            continue;
        }

        if token == "(" {
            stack.push(token);
            continue;
        }

        if token == ")" {
            while let Some(op) = stack.pop() {
                if op == "(" {
                    break;
                } else {
                    queue.push(op)
                }
            }
            continue;
        }
    }

    while let Some(op) = stack.pop() {
        queue.push(op)
    }

    queue
}

#[cfg(test)]
mod tests {
    use crate::tokenizer::tokenize;

    use super::*;

    #[test]
    fn test_shunt_yard() {
        let test_expression = tokenize(String::from("3 + 18 - 40 * (25 / 22 + 4)"));
        let expected_tokens: Vec<String> = tokenize(String::from("3 18 + 40 25 22 / 4 + * -"));
        let result_tokens = shunt_yard(test_expression);

        assert_eq!(result_tokens, expected_tokens);
    }
}
