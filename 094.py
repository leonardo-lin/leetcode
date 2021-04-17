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
        #print(root.val)
        #print(root.left.val)
        #print(root.right.val)
        #print(root,root.right,root.left)
        def inorder(self,node):
            if node.left!=None:
                inorder(self,node.left)
            ans.append(node.val)
            if node.right!=None:
                inorder(self,node.right)
        inorder(self,root)
        return ans
def main():
    side= Solution
    e=TreeNode(5,None,None)
    a=TreeNode(4,None,None)
    b=TreeNode(3,a,e)
    c=TreeNode(2,None,None)
    d=TreeNode(1,c,b)
    #print(d.val)
    print(side.inorderTraversal(side,c))
    
    

if __name__ == "__main__":
    main()