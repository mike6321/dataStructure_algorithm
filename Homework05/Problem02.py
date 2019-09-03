class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        #마지막에 노드 추가
        self.data.append(item)
        # 마지막 인덱스 기억
        i = len(self.data) -1
        # 루트까지 지속해서 만복
        while i >1 : 
            if self.data[i] > self.data[i//2]: # 부모 노드의 번호 : m//2
                self.data[i],self.data[i//2] = self.data[i//2],self.data[i]
                i = i//2
            else:
                break

def solution(x):
    return 0