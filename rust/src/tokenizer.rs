static VALID_TOKENS: [char; 6] = ['+', '-', '*', '/', '(', ')'];

pub fn tokenize(line: String) -> Vec<String> {
    let mut line_tokenized: Vec<String> = vec![];
    let mut number = String::new();

    for c in line.chars() {
        if c.is_digit(10) {
            number.push(c);
        } else {
            if !number.is_empty() {
                line_tokenized.push(number.clone());
                number.clear();
            }

            if VALID_TOKENS.contains(&c) {
                line_tokenized.push(c.to_string());
            }
        }
    }

    if !number.is_empty() {
        line_tokenized.push(number);
    }

    line_tokenized
}
