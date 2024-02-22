
class Solution:
    
    def numSplits2(self, s):
        ans = 0
        left_sets = []
        right_sets = [0]*len(s)
        print(right_sets)
        st = set()
        for i in range(len(s)):
            st.add(s[i])
            left_sets.append(len(st))
        st = set()
        for i in range(len(s)-1,-1,-1):
            st.add(s[i])
            right_sets[i]=(len(st))
        for i in range(len(s)-1):
            if left_sets[i]==right_sets[i+1]:
                ans+=1
        print(left_sets,right_sets)
        return ans


def main():
    side= Solution
    print(side.numSplits2(side,'abcd'))
    

if __name__ == "__main__":
    main()        