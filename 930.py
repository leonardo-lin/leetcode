# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:31:57 2021

@author: leo
"""
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_score(nums,goal):
        tail=0
        last_tail=0
        head=0
        head1=0
        sum=0
        #score = [0 for i in range(len(nums))]
        score = 0
        for last in range(len(nums)):
            sum+=nums[last]
            while sum>goal:
                print(head)
                if head == len(nums):
                    break
                sum = sum  - nums[head]
                head+=1
                
                pass
            print(last,head)
            score += last - head + 1
        print('score:',score)     
        return score
class Solution(object):
    
    def numSubarraysWithSum(self, nums, goal):
        if goal==0:
            return sum_score(nums,goal)
        return sum_score(nums,goal) - sum_score(nums,goal-1)
        
            
        




def main():
    side= Solution
    #print(p=='apple')
    #print(side.strStr(side,'hello','ll'))
    
    
    #print(side.numSubarraysWithSum(side,[1,0,1,0,1],2))
    print()
    print(side.numSubarraysWithSum(side,[0,0,0,0,0],0))
    

if __name__ == "__main__":
    main()
    
    