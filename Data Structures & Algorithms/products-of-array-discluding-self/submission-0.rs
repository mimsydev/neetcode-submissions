impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let vec_len = nums.len();
        let mut suf_vec = vec![1i32;vec_len];
        let mut pref_vec = suf_vec.clone();
        let mut out_vec = suf_vec.clone();
        for i in 1..vec_len {
            let vec_len = vec_len as usize;
            pref_vec[i] = pref_vec[i-1] * nums[i-1];
            suf_vec[vec_len - (i+1)] = suf_vec[vec_len - i] * nums[vec_len - i];
        }
        suf_vec.iter().zip(pref_vec.iter()).map(|(a, b)| a*b).collect()
    }
}
