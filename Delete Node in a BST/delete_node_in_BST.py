'''Delete Node in a BST'''
class TreeNode:
    '''Tree node'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''Solution'''
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''Delete node in BST'''
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
                return root
            if root.left is None:
                root = root.right
                return root
            if root.right is None:
                root = root.left
                return root
            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root

    def find_min(self, root):
        '''find minimum of the tree'''
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr
