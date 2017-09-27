fn main() {
    let mut number = 3;
    let mut answer = 0;
    while number < 1000 {
        if number % 3 ==  0 {
            answer = answer + number;
        } else if number % 5 == 0 {
            answer = answer + number;
        }
        number = number + 1;
    }

    println!("{}", answer);
}
