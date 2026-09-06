# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def good(root,maxval):
            nonlocal count
            if not root: return None

            if root.val >= maxval:
                count += 1

            maxval = max(maxval,root.val)
            
            good(root.left,maxval)
            good(root.right,maxval)

        good(root,root.val)
        return count

