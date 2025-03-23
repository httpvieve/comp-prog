impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {

        let n = digits.len();
        
        // iterate from the least significant digit (right to left)
        for i in (0..n).rev() {
            if digits[i] < 9 {
                // increment then return
                digits[i] += 1;
                return digits;
            } else {
                // set to 0 and carry over
                digits[i] = 0;
            }
        }
        
        let mut result = vec![1]; // new vector starting with 1
        result.extend(digits);    // append the remaining 
        result
    
    }
}
