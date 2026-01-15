mod two_sum;
//AI Rust implementation of two-sum tester file.
fn test_two_sum() {
    let nums: [i32; 4] = [2,7,11,15];
    let target: i32 = 9;
    let result: [i32; 2] = two_sum(&nums, target);
    assert_eq!(result, [0,1]);
}

fn main() {
    test_two_sum();
}