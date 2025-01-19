class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        answer = 0
        l1 = len(nums1)
        l2 = len(nums2)
        if l1%2==0: nums2 = []
        if l2%2==0: nums1 = []
        for i in nums1:
            answer ^= i
        for i in nums2:
            answer ^= i

        return answer
        
        
def main():
    side= Solution
    
    print(side.xorAllNums(side,nums1 = [2,1,3], nums2 = [10,2,5,0]))
    

if __name__ == "__main__":
    main()