static VALID_TOKENS: [char; 6] = ['+', '-', '*', '/', '(', ')'];

pub fn lexer(line: String) -> Vec<String> {
    let mut tokens: Vec<String> = vec![];
    let mut number = String::new();

    for c in line.chars() {
        if c.is_digit(10) || c == '-' {
            number.push(c);
        } else {
            if !number.is_empty() {
                tokens.push(number.clone());
                number.clear();
            }

            if VALID_TOKENS.contains(&c) {
                tokens.push(c.to_string());
            }
        }
    }

    if !number.is_empty() {
        tokens.push(number);
    }

    tokens
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parser() {
        let test_expression = String::from("3 + 18 - 40 * (25 / 5 + 4)");
        let expected_tokens: Vec<String> = vec![
            "3", "+", "18", "-", "40", "*", "(", "25", "/", "5", "+", "4", ")",
        ]
        .into_iter()
        .map(|s| s.to_string())
        .collect();
        let result_tokens = lexer(test_expression);

        assert_eq!(result_tokens, expected_tokens);
    }
}
