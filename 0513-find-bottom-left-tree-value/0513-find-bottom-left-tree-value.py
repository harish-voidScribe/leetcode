# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = [0, 0]
        def traverse(node, level):
            if not node:
                return
            traverse(node.left, level + 1) 
            traverse(node.right, level + 1)
            nonlocal res
            if level > res[0]:   
                res = [level, node.val]
        traverse(root, 1)
        return res[1]
        