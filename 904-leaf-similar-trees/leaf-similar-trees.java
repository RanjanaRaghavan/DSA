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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        ArrayList<Integer> one = new ArrayList<>();
        ArrayList<Integer> two = new ArrayList<>();

        dfs(root1,one);
        dfs(root2,two);

        return one.equals(two);
        
    }

    public void dfs(TreeNode node, ArrayList arr){

        if(node == null){
            return;
        }

        if(node.left == null && node.right == null){
            arr.add(node.val);
        }

        if(node.left != null){
            dfs(node.left,arr);
        }

        if(node.right != null){
            dfs(node.right,arr);
        }

    }
}