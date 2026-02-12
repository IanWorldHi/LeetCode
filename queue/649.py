from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queueR = deque() #u can put a list in the brackets 
        queueD = deque()
        #.append, .popleft, .appendleft
        for i in range(len(senate)):
            if senate[i] =='R':
                queueR.append(i)
            else:
                queueD.append(i)
        while len(queueR)!=0 and len(queueD)!=0:
            if queueR[0] < queueD[0]:
                queueD.popleft()
                queueR.append(queueR[0]+n)
                queueR.popleft()
            else:
                queueR.popleft()
                queueD.append(queueD[0]+n)
                queueD.popleft()
        if len(queueR) ==0:
            return "Dire"
        elif len(queueD) ==0:
            return "Radiant"
        return ""

        





