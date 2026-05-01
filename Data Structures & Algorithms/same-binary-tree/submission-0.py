# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self,root:Optional[TreeNode])-> List[List]:
        if root is None:
            return
        q = deque([root])
        result = [[]]
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    level.append(None)
                    break
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            result.append(level)
        return result

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result1 = self.bfs(p)
        result2 = self.bfs(q)
        if result1 == result2:
            return True
        return False