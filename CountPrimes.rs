impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        let n: usize = n as usize;
        if (n < 3) {
            return 0;
        }
        let mut p = vec![true; n];
        p[0] = false;
        p[1] = false;

        (4..n).step_by(2).for_each(|e| p[e] = false);

        let mut i: usize = 3;

        while (i * i < n) {
            if p[i] == true {
                (i*i..n).step_by(i*2).for_each(|x| p[x] = false);
            }
            i += 2;
        }

        return ((3..n).step_by(2).filter(|&v| p[v]).count() + 1) as i32;
    }
}