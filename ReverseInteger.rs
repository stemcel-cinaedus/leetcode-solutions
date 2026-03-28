impl Solution {
    pub fn reverse(x: i32) -> i32 {
     let mut x_copy = x;
     let mut z: i32 = 0;

     while x_copy != 0 {
        let digit: i32 = x_copy % 10;
        x_copy /= 10;

        if let Some(new_z) = z.checked_mul(10).and_then(|v| v.checked_add(digit)) {
            z = new_z;
        } else {
            return 0;
        }
     }
    return z;
    }
}