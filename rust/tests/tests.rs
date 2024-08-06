use rust::lexer::lexer;
use rust::parser::parser;

fn eval_exp(test_expression: String) -> i64 {
    let tokens = lexer(test_expression);
    let tree = parser(tokens);

    tree.evaluate()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let test_expression = String::from("3 + 18 - 40 * (25 / 5 + 4)");
        let expected_result = -339;

        let tokens = lexer(test_expression);
        let tree = parser(tokens);
        let result = tree.evaluate();

        assert_eq!(result, expected_result);
    }

    #[test]
    fn test_0() {
        let test_expression = String::from("1 + 3");
        let expected_result = 4;

        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_1() {
        let test_expression = String::from("1 + 2 * 3");
        let expected_result = 7;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_2() {
        let test_expression = String::from("4 / 2 + 7");
        let expected_result = 9;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_3() {
        let test_expression = String::from("1 + 2 + 3 * 4");
        let expected_result = 15;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_4() {
        let test_expression = String::from("(1 + 2 + 3) * 4");
        let expected_result = 24;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_5() {
        let test_expression = String::from("(10 / 3 + 23) * (1 - 4)");
        let expected_result = -78;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_6() {
        let test_expression = String::from("((1 + 3) * 8 + 1) / 3");
        let expected_result = 11;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_7() {
        let test_expression = String::from("58 - -8 * (58 + 31) - -14");
        let expected_result = 784;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_8() {
        let test_expression = String::from("-71 * (-76 * 91 * (10 - 5 - -82) - -79)");
        let expected_result = 42714523;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_9() {
        let test_expression = String::from("10 * 20 + 3 * 7 + 2 * 3 + 10 / 3 * 4");
        let expected_result = 239;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_10() {
        let test_expression = String::from("(-13 - -73) * (44 - -78 - 77 + 42 - -32)");
        let expected_result = 7140;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_11() {
        let test_expression = String::from("-29 * 49 + 47 - 29 + 74 - -85 - -27 + 4 - 28");
        let expected_result = -1241;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_12() {
        let test_expression = String::from("-74 - -14 + 42 - -4 + -78 + -50 * -35 * -81 + -41");
        let expected_result = -141883;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_13() {
        let test_expression = String::from("80 * -18 * (85 * (-46 + -71) - 12 + 26 - 59) + 84");
        let expected_result = 14385684;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_14() {
        let test_expression = String::from("25 + 38 + 88 + (-6 - -73) * (-83 + (53 + 97) * 14)");
        let expected_result = 135290;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_15() {
        let test_expression = String::from("(84 - 90) * (-8 - 75 + -83 * (56 - -77) + 4 + -94)");
        let expected_result = 67272;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_16() {
        let test_expression = String::from("(54 - -8 - -35 + -68 - -90) * -39 + -43 + -91 * -30");
        let expected_result = -1954;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_17() {
        let test_expression =
            String::from("-13 - -74 + (66 + -57) * -93 * -9 * 77 + 79 - 66 + -53");
        let expected_result = 580062;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_18() {
        let test_expression =
            String::from("(-72 - 50 * -74 + -45) * 92 * 21 * 5 * (-13 - 66 - 18)");
        let expected_result = -3357342660;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_19() {
        let test_expression =
            String::from("-7 - -37 * (90 + 70) - 30 - -44 + -32 - 56 - -48 - -78");
        let expected_result = 5965;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_20() {
        let test_expression =
            String::from("65 * -83 - -3 + -20 + 24 - 85 * (-24 + -32) * (61 - 20)");
        let expected_result = 189772;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_21() {
        let test_expression =
            String::from("55 * 48 * -44 - -32 + 1 * -80 * -94 - 74 * -53 + -30 + -61");
        let expected_result = -104777;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_22() {
        let test_expression =
            String::from("-82 * (25 + 62 + 3) - -72 + -65 * -32 * (77 + 12) - -95 + 51");
        let expected_result = 177958;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_23() {
        let test_expression =
            String::from("(2 - 65 - (-24 + -97) * -5 * -61) * (-41 + 85 * 9 * -92 * (75 - 18))");
        let expected_result = -147799088242;
        assert_eq!(eval_exp(test_expression), expected_result);
    }

    #[test]
    fn test_24() {
        let test_expression = String::from(
            "-20 + -51 + 20 + -68 * -11 + -35 * -14 - 95 - 32 + -52 * -23 - -90 * -42",
        );
        let expected_result = -1524;
        assert_eq!(eval_exp(test_expression), expected_result);
    }
}
