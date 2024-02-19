def areNumbersAscending(s):
    s=s.split()
    #print(s)
    temp=-1
    answer=True
    #check_output=[]
    for i in s:
        if i.isdigit():
            int_i=int(i)
            if temp>int_i:
                return False
            else:
                temp=int_i
            #check_output.append(int(i))
    
    
    #print(check_output)
    
    #isdigit()
    return answer
    
if __name__ == "__main__":
    s="hello world 5 x 5"
    target=8
    print(areNumbersAscending(s))