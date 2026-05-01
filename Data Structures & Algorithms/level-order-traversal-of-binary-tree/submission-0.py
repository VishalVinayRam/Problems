from collections import defaultdict

class Solution:
    def traversal(self, root: Optional[TreeNode], result, height):
        if root is None:
            return
        
        result[height].append(root.val)
        
        self.traversal(root.left, result, height + 1)
        self.traversal(root.right, result, height + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = defaultdict(list)
        self.traversal(root, result, 0)
        
        return [result[i] for i in range(len(result))]