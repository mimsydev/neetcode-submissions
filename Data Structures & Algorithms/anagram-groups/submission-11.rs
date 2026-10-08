impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        if strs.len() ==1 {
            let mut ret: Vec<Vec<String>> = Vec::new();
            ret.push(strs);
            return ret;
        }
        let mut maps: HashMap<[u8; 26], Vec<String>> = HashMap::new();
        for st in strs {
            let mut count = [0u8; 26];
            for c in st.bytes() {
                count[(c-b'a') as usize] += 1;
            }
            maps.entry(count).or_default().push(st.clone());
        }
        maps.into_values().collect()
    }
}
