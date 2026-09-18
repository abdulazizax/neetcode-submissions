# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        self.res = True

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 

            dfs(root.left)

            if len(nums) > 0 and nums[-1] >= root.val:
                print(nums[-1], root.val)
                self.res = False
            # print(root.val)
            nums.append(root.val)

            dfs(root.right)

        dfs(root)
        print(nums)

        return self.res

        