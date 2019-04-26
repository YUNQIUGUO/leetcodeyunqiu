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
    public boolean isBalanced(TreeNode root) {
        
        int res = dfsHeight(root);
        if (res == -1){
            return false;
        } else{
            return true;
        }   
    }
    
    // recursive DFS height function
    public int dfsHeight(TreeNode node){
            // ensure the null case
            if (node == null){
                return 0;
            }
            
            int leftHeight = dfsHeight(node.left);
            if (leftHeight == -1) {   // unbalanced
                return -1;
            }
            
            int rightHeight = dfsHeight(node.right);
            if (rightHeight == -1) {
                return -1;
            }  // unbalanced
            
            if (Math.abs(leftHeight - rightHeight) > 1)  {
                return -1;          // unbalanced definition
            }
            return Math.max(leftHeight,rightHeight) + 1; // non-negative :balanced
    }
}