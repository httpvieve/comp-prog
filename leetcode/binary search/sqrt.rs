impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x == 0 {
            return 0; // handle edge case
        }

        let mut left = 1; // start from 1 since x > 0
        let mut right = x;
        let mut result = 0;

        while left <= right {
            let mid = left + (right - left) / 2;
            let square = mid as i64 * mid as i64; // prevent overflow

            if square > x as i64 {
                right = mid - 1;
                result = mid - 1;
            } else if square < x as i64 {
                left = mid + 1;
                result = mid;
            } else {
                return mid; // exact square root found
            }
        }

        result 
    }
}
