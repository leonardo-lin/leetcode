
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n>1:
            print(n)
            if (n**0.5) % 1 == 0:
                n=n**0.5
            elif (n/2) % 1 == 0:
                n=n/2
            else:
                return False
        return True
        
def main():
    side= Solution
    
    print(side.isPowerOfTwo(side,0))
    

if __name__ == "__main__":
    main()