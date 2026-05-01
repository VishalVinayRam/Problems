class Solution:
    def traversal(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return
        
        if root.left:
            self.traversal(root.left, result)
        
        result.append(root.val)
        
        if root.right:
            self.traversal(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result