/*
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
*/


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
    public int goodNodes(TreeNode root) {
        return count_good(root, root.val);
    }
    public int count_good(TreeNode node, int max_value) {
        /* 
        Return the number of good nodes this subtree contains.
        Time: O(n) - Traversing the tree.
        Space: O(n) - In the worst case, the tree might be a line, 
            so the stack would have n calls.
        */
        // Base case: if there is no node, it isn't good.
        if (node == null) {
            return 0;
        }
        // Start counting good nodes.
        int count = 0;
        // First check if the current node is good.
        if (node.val >= max_value) {
            count += 1;
            // If it's good, it must be the new max value.
            max_value = Math.max(max_value, node.val);
        }
        // Now check how many good nodes its children has.
        int left_good_count = count_good(node.left, max_value);
        int right_good_count = count_good(node.right, max_value);
        // Sum up the result.
        return count + left_good_count + right_good_count;
    }
}
