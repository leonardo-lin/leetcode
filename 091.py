class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        if s[0]=='0':
            return 0
        for i in range(len(s)-1):
            if s[i]==s[i+1] and s[i]=='0':
                return 0
        back=1
        front=1
        #head=1
        for i in range(len(s)+1):
            if i==0 or i==1:
                continue
            """if i==2:
                temp=int(s[0:2])
                if temp<27:
                    head=2
                continue"""
            temp=int(s[i-2:i])
            print(temp)
            now=0
            print('hi',temp%10)
            if temp%10!=0 :
                now+=front
                print('po',now)
            if temp<27 and temp//10!=0:
                print(temp//10)
                now+=back
                print('ins',now)
            print(now,front,back)
            print()
            back=front
            front=now
            #head=now
        #print(front)
        #temp=int(s[len(s)-2:len(s)])

        return front
            

        

def main():
    side= Solution
    print(side.numDecodings(side,'2101'))

if __name__ == "__main__":
    main()