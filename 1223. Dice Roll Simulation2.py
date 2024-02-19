def longestSubsequence(arr, difference) :
    dic={}
    d=-difference
    for i in arr:
        #print(i)
        if i+d not in dic and i not in dic:
            dic[i]=1
            #print("1 "+str(i)+" "+str(dic[i]))
        elif i+d not in dic and i in dic:
            #print("2 "+str(i)+" "+str(dic[i]))
            continue
            
        elif i+d in dic and i in dic:
            if dic[i]<=dic[i+d]:
                dic[i]=dic[i+d]+1
            #print("3 "+str(i)+" "+str(dic[i]))
        elif i+d in dic and i not in dic:
            dic[i]=dic[i+d]+1
            #print("4 "+str(i)+" "+str(dic[i]))
    #def dp(rollMax,past_num,n,use_time):
    #print(dic)
    max=0
    for i in dic:
        if dic[i]>max:
            max=dic[i]
    return max
    
if __name__ == "__main__":
    s=[1,2,3,4]
    target=1
    print(longestSubsequence(s,-target))