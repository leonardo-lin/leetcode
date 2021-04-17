# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        
        
        ans=[]
        """def behave(self,pnode,qnode,ans):
            a=10
            if pnode==None and qnode==None:
                print('inside3')
                return 0 
            elif pnode==None or qnode==None:
                ans.append(False)
                print('inside2')
                return 0
            if pnode.val!=qnode.val:
                ans.append(False)
                print('inside')
                return 0
            behave(self,pnode.left,qnode.left,ans)
            behave(self,pnode.right,qnode.right,ans)
        behave(self,p,q,ans)
        print(ans)"""
        #if len(ans)==0:
        #    return True
        pnode=p
        qnode=q
        while qnode!=None:
            tq=qnode
            tp=pnode
            while tq!=None:
                if tp==None:
                    return False
                if tp.right ==None and tq.right!=None:
                    return False
                elif tq.right==None and tp.right!=None:
                    return False
                if tp.left ==None and tq.left!=None:
                    return False
                elif tq.left==None and tp.left!=None:
                    return False
                if tq.val!=tp.val:
                    return False
                if tq.left!=None:
                    
                    if tp.left.val!=tq.left.val:
                        return False
                tp=tp.right
                tq=tq.right
            qnode=qnode.left
            pnode=pnode.left
            
        return True

#[390,255,2266,-273,337,1105,3440,-425,4113,null,null,600,1355,3241,4731,-488,-367,16,null,565,780,1311,1755,3075,3392,4725,4817,null,null,null,null,-187,152,395,null,728,977,1270,null,1611,1786,2991,3175,3286,null,164,null,null,4864,-252,-95,82,null,391,469,638,769,862,1045,1138,null,1460,1663,null,1838,2891,null,null,null,null,3296,3670,4381,null,4905,null,null,null,-58,null,null,null,null,null,null,null,null,734,null,843,958,null,null,null,1163,1445,1533,null,null,null,2111,2792,null,null,null,3493,3933,4302,4488,null,null,null,null,null,null,819,null,null,null,null,1216,null,null,1522,null,1889,2238,2558,2832,null,3519,3848,4090,4165,null,4404,4630,null,null,null,null,null,null,1885,2018,2199,null,2364,2678,null,null,null,3618,3751,null,4006,null,null,4246,null,null,4554,null,null,null,1936,null,null,null,null,2444,2642,2732,null,null,null,null,null,null,null,4253,null,null,null,null,2393,2461,null,null,null,null,4250,null,null,null,null,2537]
#[390,255,2266,-273,337,1105,3440,-425,4113,null,null,600,1355,3241,4731,-488,-367,16,null,565,780,1311,1755,3075,3392,4725,4817,null,null,null,null,-187,152,395,null,728,977,1270,null,1611,1786,2991,3175,3286,null,164,null,null,4864,-252,-95,82,null,391,469,638,769,862,1045,1138,null,1460,1663,null,1838,2891,null,null,null,null,3296,3670,4381,null,4905,null,null,null,-58,null,null,null,null,null,null,null,null,734,null,843,958,null,null,null,1163,1445,1533,null,null,null,2111,2792,null,null,null,3493,3933,4302,4488,null,null,null,null,null,null,819,null,null,null,null,1216,null,null,1522,null,1889,2238,2558,2832,null,3519,3848,4090,4165,null,4404,4630,null,null,null,null,null,null,1885,2018,2199,null,2364,2678,null,null,null,3618,3751,null,4006,null,null,4246,null,null,4554,null,null,null,1936,null,null,null,null,2444,2642,2732,null,null,null,null,null,null,null,4253,null,null,null,null,2461,2393,null,null,null,null,4250,null,null,null,null,2537]
"""
(390, 390)
(255, 255)
(2266, 2266)
(1105, 1105)
(3440, 3440)
(3241, 3241)
(4731, 4731)
(4725, 4725)
(4817, 4817)
(4864, 4864)
(4905, 4905)
(255, 255)
(-273, -273)
(337, 337)
(-273, -273)
(-425, -425)
(4113, 4113)
(16, 16)
(-425, -425)
(-488, -488)
(-367, -367)
(-488, -488)
"""
def main():
    side= Solution
    print(side.isSameTree(side,))

if __name__ == "__main__":
    main()