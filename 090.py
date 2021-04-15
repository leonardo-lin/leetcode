class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #temp=[]
        ans=[]
        mix=[0 for x in range(len(nums))]
        #nums.sort
        #print(nums)
        nums=sorted(nums)
        print(nums)
        for i in range(2**(len(nums))):
            print(bin(i))
            i=bin(i)
            temp=[]
            for j in range(len(i)-2):
                mix[len(nums)-j-1]=i[len(i)-j-1]
            for i in range(len(nums)):
                if int(mix[i]) != 0 :
                    temp.append(int(mix[i])*int(nums[i]))
                    print(mix[i],nums[i])
                
                #print(type(mix[i]*nums[i]))
            print(temp)
            print(mix)
            if temp not in ans:
                ans.append(temp)
            print() 
        print(mix,nums)   
            #if temp not in ans:
            #    ans.append(temp)
        #ans.pop(0)
        return ans
            


def main():
    side= Solution    
    print(side.subsetsWithDup(side,[4,4,4,1,4]))

if __name__ == "__main__":
    main()