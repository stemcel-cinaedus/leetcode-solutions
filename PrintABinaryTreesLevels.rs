use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
  pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut q = VecDeque::new();
        let mut levels = Vec::new();
        match root {
            None => (),
            Some(node) => { q.push_back(node) }
        }
        loop {
            let len = q.len();
            if len == 0 {
                break;
            }
            let mut i = 0;
            let mut level = Vec::new();
            while i < len {
                let b = q.pop_front().unwrap();
                q.extend(b.borrow().left.clone());
                q.extend(b.borrow().right.clone());
                level.push(b.borrow().val);
                i += 1;
            }
            levels.push(level);
        }
        levels

    }
}