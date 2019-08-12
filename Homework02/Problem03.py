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


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        #첫번째 노드를 제거할때
        if pos == 1:
            delete = self.head     #현재 헤드의 값을 삭제할 노드에 저장
            self.head = self.head.next  #헤드의 값을 다음 노드로 변경
            return delete.data

        #첫번째 노드를 제거하는 것이 아닐 때
        else:
            #마지막노드를 제거할 때
            if pos == self.nodeCount:
                delete = self.tail #마지막 노드를 삭제할 노드에 저장
                self.tail = self.getAt(pos - 1) #tail을 현재 pos의 -1 의 방으로 지정
                self.tail.next = None   # 꼬리 다음 노드를 None으로 초기화

            else:
                delete = self.getAt(pos)
                prev = self.getAt(pos - 1)
                prev.next = self.getAt(pos).next

            self.nodeCount -= 1
            return delete.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0