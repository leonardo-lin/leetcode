# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head.next==None:
            return head
        count=1
        l=0
        r=0
        last=0
        start=0
        now=head
        """count=0
        while count<5:
            print(now.val)
            now=now.next
            count+=1"""
        print('all')
        count=1
        now=head
        while 1:

            if count==left-1:
                start=now
            if count==left:
                l=now
            print(count,right)
            if count==right:
                r=now
                last=r.next
                print('in2')
                break
            print(count,now.val)
            now=now.next
            count+=1
        if left==1:
            start=None
        
        #print(l.val,r.val,start.val,last.val)
        """tmp=head
        count=0
        while count<5:
            print(tmp.val)
            tmp=tmp.next
            count+=1"""
        now=l
        #print(now.val)
        back=last
        if head!=now:
            start.next=r
        #start.next=r
        ford=l.next
        while now != r:
            print('in',now.val)
            now.next=back
            back=now
            now=ford
            ford=now.next
        now.next=back
        back=now
        now=ford
        if(now!=None):
            ford=now.next
        if left==1:
            head=r 
            print(head.val)
        now=head
        count=0
        while count<2:
            print('*',now.val)
            now=now.next
            count+=1
        return head





def main():
    side= Solution
    e=ListNode(5,None)
    a=ListNode(4,e)
    b=ListNode(3,a)
    c=ListNode(2,b)
    d=ListNode(1,c)
    
    print(side.reverseBetween(side,a,1,2))
    
    

if __name__ == "__main__":
    main()
    