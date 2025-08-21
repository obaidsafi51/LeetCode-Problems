# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_h = right_h = 0
        left , right = root, root

        while left:
            left_h += 1
            left = left.left
        while right:
            right_h +=1
            right = right.right
        if left_h == right_h:
            return (1 << left_h) - 1 
        
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)
