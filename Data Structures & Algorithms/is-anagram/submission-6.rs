impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut char_vec_s = vec![0u8;26];
        for c in s.bytes() {
            let c = c as usize;
            char_vec_s[c-b'a' as usize] += 1;
        }
        let mut char_vec_t = vec![0u8;26];
        for c in t.bytes() {
            let c = c as usize;
            char_vec_t[c-b'a' as usize] += 1;
        }
        char_vec_s == char_vec_t
    }
}
