#def找房間
#def更新結束時間

class Solution(object):
    def mostBooked(self, n,meetings):
        meetings = sorted(meetings, key=lambda x: x[0])
        for i in range(len(meetings)):
            meetings[i].append(meetings[i][1]-meetings[i][0])
        #print(meetings)
        room = [[0,0] for i in range(n)]#結束時間和使用次數
        for meeting in meetings:
            empty = False
            short_room = [0,999999999999999999999999]#房間代碼&最早時間
            #有空房間可以用
            for i in range(len(room)):
                
                if short_room[1]>room[i][0]:
                    
                    short_room[0]=i
                    short_room[1]=room[i][0]
                    #print(short_room)
                
                if meeting[0]>=room[i][0]:
                    room[i][0] = meeting[1]
                    room[i][1] += 1
                    #print("empty room")
                    empty = True
                    break
                
            if empty==False:
                #print("full_room",room,short_room)
                room[short_room[0]][0] += meeting[2]
                room[short_room[0]][1] +=1
                
        answer = 0
        num_temp = 0
        print(room)
        for i in range(len(room)):
            if  num_temp < room[i][1]:
                num_temp = room[i][1]
                answer = i
        return answer      
def main():
    side= Solution
    
    print(side.mostBooked(side,2,[[0,10],[1,5],[2,7],[3,4]]))

if __name__ == "__main__":
    main()