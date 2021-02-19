# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:55:24 2021

@author: leo
"""
"""dict = {'Name': 'Za(ra', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
a=12
lib = {-1:1}
lib[a] = -12
print(lib[a])"""
class Solution:
    def twoSum (self, nums, target):
        lib = {}
        i=0
        for n in nums:
            #temp=target-n
            if n not in lib:
                lib[target-n]=i
                i+=1
            else:
                return [lib[n],i]
def main():
    side= Solution
    print(side.twoSum(side,[2,11,15,-2],9))
        

if __name__ == "__main__":
    main()
    
