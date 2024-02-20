
class Solution(object):
    def missingNumber(self, nums):
        l = [0 for i in range(len(nums)+1)]
        for i in nums:
            l[i] = 1
        #print(l)
        for i in range(len(l)):
            if l[i] == 0:
                return i
        
        
        
def main():
    side= Solution
    
    print(side.missingNumber(side,[3,0,1]))
    

if __name__ == "__main__":
    main()