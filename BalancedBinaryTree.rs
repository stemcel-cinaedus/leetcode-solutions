// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::cmp::max;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        pub fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) -> (bool, usize) {
            match root {
                None => return (true, 0),
                Some(node) => {
                    let left = dfs(&node.borrow().left);
                    let right = dfs(&node.borrow().right);
                    let height = max(left.1, right.1);
                    if !left.0 || !right.0 || (left.1 as isize - right.1 as isize).abs() as usize >= 2 {
                        return (false, height)
                    } else { return (true, 1 + height) }

                }
            }
        }
        return dfs(&root).0
    }
}