//Non-AI Rust implementation of two-sum.
fn two_sum(nums: &[i32], target : i32) {
    let solution: [i32, 2] = [0,0];
    let indx1: i32 = 0;
    let indx2: i32 = indx1 + 1;
    while indx1 < nums.len() {
        if nums[indx1] + nums[indx2] == target {
            solution[0] = indx1;
            solution[1] = indx2;
            return solution;
        }
        else {
            if indx2+1 == nums.len() {
                indx1 = indx1 + 1;
                indx2 = indx1 + 1;
            }
            else {
                indx2 = indx2 + 1;
            }
        }
    }
    return solution;
}