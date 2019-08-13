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


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
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
    '''
    popAfter(prev) 는 인자 prev 에 의하여 주어진 node 의 다음에 있던 node 를 삭제하고, 
    popBefore(next) 는 인자 next 에 의하여 주어진 node 의 이전에 있던 node 를 삭제합니다. 
    그리고 삭제되는 node 에 담겨 있던 data item 을 리턴합니다.
    '''
    def popAfter(self, prev):
        current_node = prev.next #현재노드에
        next_node = current_node.next
        prev.next = next_node
        next_node.prev = prev
        self.nodeCount -= 1
        return current_node.data

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            prev = self.getAt(pos - 1)
            return self.popAfter(prev)


def solution(x):
    return 0