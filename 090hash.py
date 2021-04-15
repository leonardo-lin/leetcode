class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #temp=[]
        ans=[   ]
        mix=[0 for x in range(len(nums))]
        #nums.sort
        #print(nums)
        nums=sorted(nums)
        lib={}
        #print(nums)
        def fue(nums,forin,i,ans,now):
            print(now)
            print()
            if i==len(nums):
                #if now not in ans:
                ans.append(now)
                print('end',now)
                return
            temp1=now[:]
            temp2=now[:]
            #temp1.append(nums[i]) 
            #fue(nums,1,i+1,ans,temp1)
            #fue(nums,0,i+1,ans,temp2)
            if i==0:
                #print('in2')
                temp1.append(nums[i]) 
                fue(nums,1,i+1,ans,temp1)
                fue(nums,0,i+1,ans,temp2)
            elif nums[i] != nums[i-1]:
                
                temp1.append(nums[i]) 
                print('*',temp1,temp2)
                fue(nums,1,i+1,ans,temp1)
                fue(nums,0,i+1,ans,temp2)   
            elif nums[i] == nums[i-1]:
                if forin ==1:
                    temp1.append(nums[i])
                    fue(nums,1,i+1,ans,temp1)
                    fue(nums,0,i+1,ans,temp2)
                elif forin==0:
                    fue(nums,0,i+1,ans,temp2)
                    #print('hihi',temp2)
            
        fue(nums,-1,0,ans,[])
        print(ans)    
        
        return ans
            


def main():
    side= Solution
    print(side.subsetsWithDup(side,[1,2,3,3]))

if __name__ == "__main__":
    main()