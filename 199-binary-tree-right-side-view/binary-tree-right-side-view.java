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
    public List<Integer> rightSideView(TreeNode root) {

        Queue <TreeNode> Q = new LinkedList<>();
        List <Integer> arr = new ArrayList<>();

        if(root != null){
            Q.add(root);
        }

        while(!Q.isEmpty() ){

            int cur_size = Q.size();

            for(int i=0;i<cur_size;i++){

                TreeNode node = Q.poll();

                if(i == cur_size -1){
                    arr.add(node.val);
                }

                if(node.left != null){
                    Q.add(node.left);
                }

                if(node.right != null){
                    Q.add(node.right);
                }


            }

        }

        return arr;
        
    }
}