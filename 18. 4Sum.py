
def fourSum(nums,target):
    answer=[]
    nums=sorted(nums)
    l=len(nums)
    for i in range(l-3):
        for j in range(i+1,l-2):
            head=j+1
            tail=l-1
            while(head<tail):
                if nums[i]+nums[j]+nums[head]+nums[tail]==target:
                    if [nums[i],nums[j],nums[head],nums[tail]] not in answer:
                        answer.append([nums[i],nums[j],nums[head],nums[tail]])
                    print(nums[i],nums[j],nums[head],nums[tail])
                    print("answer",i,j,head,tail)
                    head+=1
                    tail-=1
                elif nums[i]+nums[j]+nums[head]+nums[tail]>target:
                    tail-=1
                    print(nums[i],nums[j],nums[head],nums[tail])
                    print("big")
                elif nums[i]+nums[j]+nums[head]+nums[tail]<target:
                    head+=1
                    print(nums[i],nums[j],nums[head],nums[tail])
                    print("small")
    return answer          
    pass
    
        
        #1,2,2,2,2,2,5
if __name__ == "__main__":
    num=[2,2,2,1,2,2,5]
    target=8
    print(fourSum(num,target))
