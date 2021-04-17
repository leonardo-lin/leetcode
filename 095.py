# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        
        ans=[] 
        def inorder(self,node):
            a=10
            if node.left!=None:
                inorder(self,node.left)
            ans.append(node.val)
            if node.right!=None:
                inorder(self,node.right)
        inorder(self,root)
        print(ans)
        return ans
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        ans=self.generateTreesDFS(self,1, n)
        #self.inorderTraversal(self,ans[0])
        #self.inorderTraversal(self,ans[1])
        #self.inorderTraversal(self,ans[2])
        return ans

    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(self,left, i - 1)
            right_nodes = self.generateTreesDFS(self,i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res


def main():
    side= Solution
    print(side.generateTrees(side,3))

if __name__ == "__main__":
    main()