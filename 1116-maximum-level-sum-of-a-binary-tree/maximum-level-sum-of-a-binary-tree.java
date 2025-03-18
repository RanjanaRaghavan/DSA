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
    public int maxLevelSum(TreeNode root) {

        Queue <TreeNode> Q = new LinkedList<>();
        if(root != null){
            Q.add(root);
        }

        int max_sum = Integer.MIN_VALUE;

        int level = 0;
        int max_level = 0;

        while(!Q.isEmpty()){

            int sum =0;
            level++;

            int cur_level_size = Q.size();

            for(int i=0;i<cur_level_size;i++){

                TreeNode node = Q.poll();
                sum += node.val;

                if(node.left != null){
                    Q.add(node.left);
                }

                if(node.right != null){
                    Q.add(node.right);
                }
            }

            if(sum > max_sum){
                max_sum = sum;
                max_level = level;
            }
        }
        return max_level;
    }
}