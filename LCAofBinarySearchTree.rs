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
impl Solution {
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        match p.clone() {
            None => { (return root) },
            Some(node) => {
                if (&node.borrow().val > &root.clone().unwrap().borrow().val) {
                    if &q.clone().unwrap().borrow().val > &root.clone().unwrap().borrow().val {
                        Self::lowest_common_ancestor(root.unwrap().borrow().right.clone(), p, q)
                    } else { return root }
                } else if (&node.borrow().val == &root.clone().unwrap().borrow().val) {
                    return root
                } else {
                    if &q.clone().unwrap().borrow().val < &root.clone().unwrap().borrow().val {
                        Self::lowest_common_ancestor(root.unwrap().borrow().left.clone(), p, q)
                    } else { return root }
                }
            }
        }
    }
}