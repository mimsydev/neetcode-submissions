impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result_map: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {  
            let diff = target - nums[i];
            let i_i32 = i as i32;
            if let Some(j) = result_map.get(&diff) {
                return vec![*j, i_i32];
            } else {
                result_map.insert(nums[i], i_i32);
            }
        }
        vec![0]
    }
}
