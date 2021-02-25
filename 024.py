# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:31:57 2021

@author: leo
"""
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        fir=head
        sec=head.next
        fir.next=sec.next
        sec.next=fir
        head=sec
        if head.next.next==None:
            return head
        tmp=fir
        fir=sec
        sec=tmp
        
        #change=0
        while(1):
            if sec.next==None:
                print(head.val,'\n',head.next.val,'\n',head.next.next.val,'\n',head.next.next.next.val)
                return head
            elif sec.next.next==None:
                print(head.val,'\n',head.next.val,'\n',head.next.next.val,'\n',head.next.next.next.val)
                return head
            else:
                a=sec.next
                b=sec.next.next
                a.next=b.next
                b.next=a
                sec.next=b
                fir=b
                sec=a
        
        
        """while (1):
            print(nec.val) 
            if change==0:
                nec=fir.next
                fir.next=nec
                sec.next=fir
                sec=fir.next
                #nec=nec.next
                change=1
            elif change==1:
                fir=fir.next
                sec=sec.next
                change=0
            print(nec.val)     
            
            if nec==None:
                break
            nec=nec.next"""
            
        




def main():
    side= Solution
    #print(p=='apple')
    #print(side.strStr(side,'hello','ll'))
    e=ListNode(5,None)
    a=ListNode(4,e)#4321
    b=ListNode(3,a)
    c=ListNode(2,b)
    d=ListNode(1,c)
    
    print(side.swapPairs(side,d))
    print()
    

if __name__ == "__main__":
    main()
    
    