impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut count: HashMap<i32, i32> = HashMap::new();
        for n in nums {
            *count.entry(n).or_insert(0i32) += 1;
        }

        let mut heap = BinaryHeap::new();
        for (num, freq) in count {
            heap.push(Reverse((freq, num)));
            if heap.len() > k {
                heap.pop();
            }
        }

        heap.into_iter().map(|Reverse((_, num))| num).collect()

    }
}
