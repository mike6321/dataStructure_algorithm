class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def postorder(self):
        trav = []

        if self.left:
            trav += self.left.postorder()
        if self.right:
            trav += self.right.postorder()

        trav.append(self.data)

        return trav


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(x):
    return 0