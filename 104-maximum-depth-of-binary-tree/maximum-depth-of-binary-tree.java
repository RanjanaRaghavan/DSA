/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        
       return dfs(root,0);
    }

    public int dfs(TreeNode node, int cur_count){

        if(node == null){
            return cur_count;
        }

        cur_count++;

        int left = dfs(node.left,cur_count);
        int right = dfs(node.right,cur_count);

        return Math.max(left,right);

    }
}