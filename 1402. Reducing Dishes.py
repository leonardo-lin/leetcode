def maxSatisfaction(satisfaction):
    
    satisfaction=sorted(satisfaction)
    answer=0
    total=sum(satisfaction)
    sum_list=[]
    for i in range(len(satisfaction)):
        sum_list.append(total)
        total-=satisfaction[i]
    #print(sum_list)
    
    answer=sum(sum_list)
    temp=sum(sum_list)
    for i in range(len(sum_list)):
        temp-=sum_list[i]
        if temp>answer:
            answer=temp
    return answer
    pass
    
if __name__ == "__main__":
    num=[-1,-8,0,5,-9]
    target=8
    print(maxSatisfaction(num))