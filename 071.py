class Solution(object):
    def climbingStairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        back=0
        temp1=1
        for i in range(s+1):
            if i == 0:
                back=1
            elif i == 1:
                front=1
            else:
                temp=front+back
                back=front
                front=temp
                print(front,back)
        return front

def main():
    side= Solution
    print(side.clibingStairs(side,2))

if __name__ == "__main__":
    main()