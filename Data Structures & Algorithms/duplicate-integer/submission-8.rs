impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let v_len = nums.len();
        let h_set: HashSet<i32> = nums.into_iter().collect();
        v_len != h_set.len()
    }
}
