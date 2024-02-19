def dieSimulator(n, rollMax):
    def dp(rollMax,past_num,n,use_time):
        cnt=0
        #print(past_num,n)
        if n==0:return 1
        #print(n)
        if past_num==0:
            
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,0,n-1,use_time+1)
            cnt+=dp(rollMax,1,n-1,1)
            cnt+=dp(rollMax,2,n-1,1)
            cnt+=dp(rollMax,3,n-1,1)
            cnt+=dp(rollMax,4,n-1,1)
            cnt+=dp(rollMax,5,n-1,1)
        if past_num==1:
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,1,n-1,use_time+1)
            cnt+=dp(rollMax,0,n-1,1)
            cnt+=dp(rollMax,2,n-1,1)
            cnt+=dp(rollMax,3,n-1,1)
            cnt+=dp(rollMax,4,n-1,1)
            cnt+=dp(rollMax,5,n-1,1)
        if past_num==2:
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,2,n-1,use_time+1)
            cnt+=dp(rollMax,1,n-1,1)
            cnt+=dp(rollMax,0,n-1,1)
            cnt+=dp(rollMax,3,n-1,1)
            cnt+=dp(rollMax,4,n-1,1)
            cnt+=dp(rollMax,5,n-1,1)
        if past_num==3:
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,3,n-1,use_time+1)
            cnt+=dp(rollMax,1,n-1,1)
            cnt+=dp(rollMax,2,n-1,1)
            cnt+=dp(rollMax,0,n-1,1)
            cnt+=dp(rollMax,4,n-1,1)
            cnt+=dp(rollMax,5,n-1,1)
        if past_num==4:
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,4,n-1,use_time+1)
            cnt+=dp(rollMax,1,n-1,1)
            cnt+=dp(rollMax,2,n-1,1)
            cnt+=dp(rollMax,3,n-1,1)
            cnt+=dp(rollMax,0,n-1,1)
            cnt+=dp(rollMax,5,n-1,1)
        if past_num==5:
            if use_time<rollMax[past_num]:
                cnt+=dp(rollMax,5,n-1,use_time+1)
            cnt+=dp(rollMax,1,n-1,1)
            cnt+=dp(rollMax,2,n-1,1)
            cnt+=dp(rollMax,3,n-1,1)
            cnt+=dp(rollMax,4,n-1,1)
            cnt+=dp(rollMax,0,n-1,1)
        
        #print(f"cnt = {cnt}")
        return cnt
    cnt=0
    cnt+=dp(rollMax,0,n-1,1)
    cnt+=dp(rollMax,1,n-1,1)
    cnt+=dp(rollMax,2,n-1,1)
    cnt+=dp(rollMax,3,n-1,1)
    cnt+=dp(rollMax,4,n-1,1)
    cnt+=dp(rollMax,5,n-1,1)

    
    return cnt%1000000007


if __name__ == "__main__":
    s=[6,6,2,2,2,1]
    target=10
    print(dieSimulator(target,s))