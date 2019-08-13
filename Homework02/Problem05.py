
#reverse 구현
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    #def reverse(self):
        '''
        temp = None #바꿀값을 저장할 변수
        curr = self.head
        answer = []
        answer.append(curr.data) #현재의 값을 append

        while curr:
            temp = curr.prev  #현재 curr의 이전값을 temp에 저장
            curr.prev = curr.next   #현재 이전 노드는 현재 다음 노드
            curr.next = temp
            curr = curr.prev
            answer.append(curr.data)
        if temp:
            self.head = temp.prev

        return answer
        '''

    def reverse(self):
        result = []
        curr = self.tail
        # key Point!
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)

        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


def solution(x):
    return 0