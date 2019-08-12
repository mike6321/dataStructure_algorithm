class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def insertAt(self,pos,newNode):
        if pos < 1 or pos > self.nodeCount+1:
            return False
        #헤드에 넣을때
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        #중간에 넣을때
        else:
            if pos == self.nodeCount+1:
                prev = self.tail
            else:
                prev = self.getAt(pos-1)
            newNode.next = prev.next
            prev.next = newNode

        #마지막에 넣을때
        if pos == self.nodeCount+1:
            self.tail = newNode

        self.nodeCount +=1

        return  True

    def traverse(self):
        answer = []
        cur = self.head

        #그 다음 값이 None이 아닐때 까지 탐색 합니다.
        while cur is not None:
            answer.append(cur.data)
            cur = cur.next
        return answer
        '''
        잘못된 방법 : 두번째 찾을 때 1,2 세번째 찾을때  1,2,3 방문 -> 그냥 다음다음으로 탐색하게끔 
        i=1
        while i<=self.nodeCount:
            answer.append(self.getAt(i))
        return answer 
        '''
# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0