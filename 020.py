# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:11:20 2021

@author: leo
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        now=0
        while(now!=len(s)):
            if (s[now]==')' or s[now]==']' or s[now]=='}') and now==0:
                #print(s)
                return False
            if s[now]==')' :
                if s[now-1]=='(':
                    s.pop(now)
                    s.pop(now-1)
                    if now==1:
                        now+=1
                    now-=3
                    #print(now)
            elif s[now]==']' :
                if s[now-1]=='[':
                    s.pop(now)
                    s.pop(now-1)
                    if now==1:
                        now+=1
                    now-=3
                    #print(s)
            elif s[now]=='}' :
                if s[now-1]=='{':
                    s.pop(now)
                    s.pop(now-1)
                    if now==1:
                        now+=1
                    now-=3
                    #print(s)
            now+=1
        if len(s)==0:
            return True
        #print(s,'hi')
        return False
            