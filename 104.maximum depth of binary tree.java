/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        return depth(root,0);         // here it's a zero!
    }
    
    int depth (TreeNode node,int depth) {
        if (node == null){
             return depth;
        }
           
        else {
            int res = 0;
            res = Math.max(depth(node.left,depth + 1), depth(node.right,depth + 1));
            return res;
        }
            
    }
}