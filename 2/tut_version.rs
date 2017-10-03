struct Fibonacci {
    curr: u32,
    next: u32,
}

// The implementation for this is from the Rust book:
// https://rustbyexample.com/trait/iter.html

impl Iterator for Fibonacci {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        let new_next = self.curr + self.next;

        self.curr = self.next;
        self.next = new_next;

        Some(self.curr)
    }
}

fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 1, next: 1}
}

fn main() {
    let mut sum = 0;

    for i in fibonacci() {
        if i % 2 == 0 {
            sum = sum + i;
        }
        if i > 4000000 {
            break;
        }
    }
    println!("The sum is: {}", sum);
}

