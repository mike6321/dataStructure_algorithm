class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        '''
        키가 크고 작을때 분기를 태워
        왼 오 를 구별하는것이 키포인트인듯
        '''
        #키가 작을때
        if key<self.key:

            if self.left:
                self.left.insert(key, data)

            else:
                self.left = Node(key, data)

        # 키가 클때
        elif key>self.key:

            if self.right:
                self.right.insert(key, data)

            else:
                self.right = Node(key, data)


        else:
            raise KeyError('와츠고잉온...')

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0