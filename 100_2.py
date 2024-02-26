class treeNode:
    def __init__(self, val):
         # 初始化節點
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, val):
         # 如果要新增左邊節點，先檢查是否已存在，若左節點不存在則放入左節點
        if self.left == None:
            self.left = treeNode(val)
         # 如果左節點已經存在，則放入左節點的下一層左節點，這邊用遞迴的方式進行搜尋，直到可以讓入左節點為止
        else:
            self.left.insertLeft(val)
    
    def insertRight(self, val):
         # 新增右邊節點的方式則和新增左節點的方式相同
        if self.right == None:
            self.right = treeNode(val)
        else:
            self.right.insertRight(val)
def mid_search(p,li):
    
    pr=None
    pl=None
    if p.left!=None:
        pl=p.left.val
    if p.right!=None:
        pr=p.right.val
        
    if p.left!=None:
        mid_search(p.left, li)
    
    print(p)
    li.append([p.val,pl,pr])
    
    if p.right!=None:
        mid_search(p.right, li)
    return(li)

def front_search(p,li):
    pr=None
    pl=None
    if p.left!=None:
        pl=p.left.val
    if p.right!=None:
        pr=p.right.val
    print(p)
    
    li.append([p.val,pl,pr])
    if p.left!=None:
        mid_search(p.left, li)

    if p.right!=None:
        mid_search(p.right, li)
    return(li)

class Solution(object):
    def swapPairs(self, p,q):
        
        p_f=[]
        q_f=[]
        p_m=[]
        q_m=[]
        p_f=front_search(p,p_f)
        print(p_f)
        q_f=front_search(q,q_f)
        print(q_f)
        if p_f==q_f:
            print('pass')
        
        p_m=mid_search(p,p_m)
        print(p_m)
        q_m=mid_search(q,q_m)
        print(q_m)
        if p_m==q_m:
            print('pass2')
        if p_f==q_f and p_m==q_m:
            return True
        else:
            return False
        
        
def main():
    side= Solution
    sampleTree = treeNode(5)
    sampleTree.insertRight(7)
    sampleTree.insertRight(8)
    sampleTree.insertLeft(3)
    sampleTree.insertLeft(2)
    sampleTree.right.insertLeft(6)
    sampleTree.left.insertRight(4)
    print(sampleTree.val)

    sampleTree2 = treeNode(5)
    sampleTree2.insertRight(7)
    sampleTree2.insertRight(8)
    sampleTree2.insertLeft(3)
    sampleTree2.insertLeft(2)
    sampleTree2.right.insertLeft(6)
    sampleTree2.left.insertRight(4)
    print(sampleTree2.val)
    
    print(side.swapPairs(side, sampleTree, sampleTree2))
if __name__ == "__main__":
     main()
    
    
# 執
