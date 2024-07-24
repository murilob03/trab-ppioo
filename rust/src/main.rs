mod tokenizer;
mod shunt_yard;

use tokenizer::tokenize;
use shunt_yard::shunt_yard;

fn main() {
    // let test_expression = String::from("3 + 2 - 1 * (4 / 6 + 7)");
    let test_expression = String::from("3 + 18 - 40 * (25 / 22 + 4)");

    let tokens = tokenize(test_expression);
    let tokens_postfix = shunt_yard(tokens);

    println!("{:?}", tokens_postfix);
}
