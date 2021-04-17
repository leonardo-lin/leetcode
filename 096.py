class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[1,1]
        i=2
        while i<=n:
            j=0
            temp=0
            while(j<i):
                print(i,j)
                temp+=(ans[j]*ans[i-j-1])
                j+=1
            ans.append(temp)
            i+=1
        print(ans)
        return(ans[len(ans)-1])

def main():
    side= Solution
    print(side.numTrees(side,5))

if __name__ == "__main__":
    main()