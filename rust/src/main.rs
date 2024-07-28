mod expression_tree;
mod shunt_yard;
mod tokenizer;

use expression_tree::Tree;
use shunt_yard::shunt_yard;
use tokenizer::tokenize;

fn main() {
    // let test_expression = String::from("3 + 2 - 1 * (4 / 6 + 7)");
    let test_expression = String::from("3 + 18 - 1 * (25 / 5 + 4)");

    let tokens = tokenize(test_expression);
    let tokens_postfix = shunt_yard(tokens);
    let exp_tree = Tree::parse_from_vector(tokens_postfix);
    // print!("{}", exp_tree.to_string());
    exp_tree.evaluate();

    // println!("Result: {}", result);
    // println!("{:?}", tokens_postfix);
}
