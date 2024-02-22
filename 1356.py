def count_bit(num):
        bits = 0
        while num >0:
            if num%2==1:
                bits += 1
                num-=1
            num /=2 
        #print(bits)
        return bits
class Solution:
    
    def sortByBits(self, arr):
        bitarr = [count_bit(x) for x in arr]
        ans = [x for _,x in sorted(zip(bitarr,arr))]
        return ans




def main():
    side= Solution
    # e=ListNode(5,None)
    # a=ListNode(4,e)
    # b=ListNode(3,a)
    # c=ListNode(2,b)
    # d=ListNode(1,c)
    
    print(side.sortByBits(side,[1024,512,256,128,64,32,16,8,4,2,1]))
    
    

if __name__ == "__main__":
    main()
    