class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self):
        q = ArrayQueue()
        trav = []

        #1. q에 루트를 add
        if self.root:
            q.enqueue(self.root)

        #2. q가 빌때까지 루트를 돈다.
        while not q.isEmpty():
            #3. 들어있는 큐 빼기
            node = q.dequeue()
            #4. 뺀 큐 순회 배열에 append
            trav.append(node.data)

            #양방향이기때문에 왼,오 나누어 큐에 집에 넣기
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

            #이러한 식으로 계속 넣다뺏다들 반복한다음 큐가 들어있지 않다면 리턴한다. [거의 공식]

        return trav


def solution(x):
    return 0