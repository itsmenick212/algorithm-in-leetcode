# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:  # preorder should have the same length as inorder
            root = TreeNode(preorder[0])
            i = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:1+i], inorder[:i])
            root.right = self.buildTree(preorder[1+i:], inorder[i+1:])
            return root
