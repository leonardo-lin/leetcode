# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:34:54 2021

@author: leo
"""

class Solution(object):
    def strSt(self, haystack, needle):
        #return haystack.find(needle)
        k=len(needle)
        q=len(haystack)
        if needle==haystack=='' or k==0:
            return 0
        if k >len(haystack):
            return -1
        h=-1
        j=0
        ##print(haystack[0],needle[1])
        for i in haystack[::]:
            h+=1
            if i==needle[0]:
                for j in range(k):
                    #if not(haystack[i+j].equal(needle[j])):
                    #print(h+j,' ',j)
                    if h+j==q:
                        break
                    elif haystack[h+j]!=needle[j]:
                        break
                    elif j==k-1:
                        return h
        return -1
    def strStr(self, haystack, needle):
        k=len(needle)
        q=len(haystack)
        if needle==haystack=='' or k==0:
            return 0
        if k >q:
            return -1
        i=0
        while q-i>=k:
            if haystack[i]==needle[0]:
                st=haystack[i:i+k]
                if st==needle:
                    return i
            i+=1
        return -1
                
            
        
        
        
def main():
    side= Solution
    #print(p=='apple')
    #print(side.strStr(side,'hello','ll'))
    print(side.strStr(side,"mississippi","issipi"))
    

if __name__ == "__main__":
    main()
    
    
    
    