impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut st = std::collections::HashMap::new();
        st.entry(0).or_insert(1);
        let mut cur_sum = 0;
        let mut tot_arrs = 0;

        for n in nums {
            cur_sum += n;
            tot_arrs += st.get(&(cur_sum - k)).unwrap_or(&0);
            *st.entry(cur_sum).or_insert(0) += 1;
        }
        tot_arrs
    }
}
