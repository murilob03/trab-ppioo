// Define the valid tokens for arithmetic expressions.
static VALID_TOKENS: [char; 6] = ['+', '-', '*', '/', '(', ')'];

// Tokenizer function to split a line of input into tokens.
pub fn lexer(line: String) -> Vec<String> {
    // Vector to store the resulting tokens.
    let mut tokens: Vec<String> = vec![];

    // String to accumulate digits for multi-digit numbers.
    let mut number = String::new();

    // Iterate through each character in the input line.
    for c in line.chars() {
        // Check if the character is part of a number or is a minus sign.
        if c.is_digit(10) || c == '-' {
            number.push(c);
        } else {
            // If there is a number accumulated, push it as a token and clear the number string.
            if !number.is_empty() {
                tokens.push(number.clone());
                number.clear();
            }

            // If the character is a valid token, convert it to a string and add it to the tokens vector.
            if VALID_TOKENS.contains(&c) {
                tokens.push(c.to_string());
            }
        }
    }

    // If there is any remaining number after the loop, add it to the tokens vector.
    if !number.is_empty() {
        tokens.push(number);
    }

    tokens
}

// Tests for the lexer function to ensure it works correctly.
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parser() {
        // Define a test expression and the expected token output.
        let test_expression = String::from("3 + 18 - 40 * (25 / 5 + 4)");
        let expected_tokens: Vec<String> = vec![
            "3", "+", "18", "-", "40", "*", "(", "25", "/", "5", "+", "4", ")",
        ]
        .into_iter()
        .map(|s| s.to_string())
        .collect();

        // Get the result from the lexer function.
        let result_tokens = lexer(test_expression);

        // Assert that the lexer output matches the expected tokens.
        assert_eq!(result_tokens, expected_tokens);
    }
}
