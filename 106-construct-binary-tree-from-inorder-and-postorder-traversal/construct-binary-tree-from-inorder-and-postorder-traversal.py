# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # map value → index for O(1) lookup
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(left, right):
            if left > right:
                return None
            
            # root is last element in postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # split inorder
            mid = idx_map[root_val]
            
            # build right first (because postorder pops from end)
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)