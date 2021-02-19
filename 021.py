# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:33:21 2021

@author: leo
"""
class ListNode(object):    
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        #ans=[0]
        head =ListNode(0,None)
        #now=head
        pre=head
        
        check=0
        while(1):
            if l1==None:
                break
            if l2==None:
                check=1
                break
            if l1.val<l2.val:
                #ans.append(l1.val)
                #now=l1
                pre.next=l1
                pre=pre.next
                l1=l1.next
            else:
                #ans.append(l2.val)
                #now=l2
                pre.next=l2
                pre=pre.next
                l2=l2.next
       
        if check==1:
            while(l1!=None):
                #ans.append(l1.val)
                #now=l1
                pre.next=l1
                pre=pre.next
                l1=l1.next
        else:
           while(l2!=None):
                #ans.append(l2.val)
                #now=l2
                pre.next=l2
                pre=pre.next
                l2=l2.next
       # ans.pop(0)
        #return ans   
        return head.next
     
def main():
    side= Solution
    #print(p=='apple')
    #print(side.strStr(side,'hello','ll'))
    print(side.mergeTwoLists(side,[1,2,4],[2,3,4]))
    a=[1,2,3,3]       
    print(a)
    a.append(4)
    print(a)
    
    

if __name__ == "__main__":
    main()