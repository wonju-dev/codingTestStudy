from collections import deque
import sys
input = sys.stdin.readline

loop = int(input())

DEFAULT = int(1e11)

class Node:
    def __init__(self, value = DEFAULT):
        if value == DEFAULT:
            self.__value = [DEFAULT, 0]
        else:
            self.__value = [value, 1]
        self.__leftChild = None
        self.__rightChild = None

    def getValue(self):
        return self.__value

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setValue(self, value):
        if self.__value[1] == 0:
            self.__value[0] = value
            self.__value[1] = 1
        elif self.__value[0] == value:
            self.__value[1] += 1


    def removeValue(self):
        if self.__value[1] > 0:
            self.__value[1] -= 1

    def setNewLeftChild(self, leftChildValue):
        leftChild = Node(leftChildValue)
        self.__leftChild = leftChild

    def setLeftChild(self, node):
        self.__leftChild = node

    def setNewRightChild(self, rightChildValue):
        rightChild = Node(rightChildValue)
        self.__rightChild = rightChild

    def setRightChild(self, node):
        self.__rightChild = node

    def removeLeftChild(self):
        self.__leftChild = None

    def removeRightChild(self):
        self.__rightChild = None

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, value):
        now = self.root

        while now != None:
            if now.getValue()[1] == 0:
                now.setValue(value)
                return
            else:
                rightChild = now.getRightChild()
                leftChild = now.getLeftChild()

                if now.getValue()[0] > value:
                    if leftChild != None:
                        now = leftChild
                    else:
                        now.setLeftChild(Node(value))
                        return
                elif now.getValue()[0] < value:
                    if rightChild != None:
                        now = rightChild
                    else:
                        now.setRightChild(Node(value))
                        return
                else:
                    now.setValue(value)
                    return

    def deleteBiggest(self):
        now = self.root
        parent = self.root

        while now != None:
            rightChild = now.getRightChild()
            if rightChild != None:
                parent = now
                now = rightChild
            else:
                break

        if now.getValue()[1] > 1:
            now.removeValue()
        else:
            leftGrandChild = now.getLeftChild()
            rightGrandChild = now.getRightChild()
            if now == self.root:
                if leftGrandChild == None and rightGrandChild == None:
                    self.root = Node()
                elif leftGrandChild != None:
                    self.root = leftGrandChild
            else:
                if leftGrandChild == None and rightGrandChild == None:
                    parent.removeRightChild()
                elif leftGrandChild != None:
                    parent.setRightChild(leftGrandChild)


    def deleteSmallest(self):
        now = self.root
        parent = self.root

        while now != None:
            leftChild = now.getLeftChild()
            if leftChild != None:
                parent = now
                now = leftChild
            else:
                break

        if now.getValue()[1] > 1:
            now.removeValue()
        else:
            leftGrandChild = now.getLeftChild()
            rightGrandChild = now.getRightChild()
            if now == self.root:
                if leftGrandChild == None and rightGrandChild == None:
                    self.root = Node()
                elif rightGrandChild != None:
                    self.root = rightGrandChild
            else:
                if leftGrandChild == None and rightGrandChild == None:
                    parent.removeLeftChild()
                elif rightGrandChild != None:
                    parent.setLeftChild(rightGrandChild)

    def getBiggestValue(self):
        now = self.root

        while now != None:
            rightChild = now.getRightChild()
            if rightChild != None:
                now = rightChild
            else:
                break

        return now.getValue()[0]

    def getSmallestValue(self):
        now = self.root

        while now != None:
            leftChild = now.getLeftChild()
            if leftChild != None:
                now = leftChild 
            else:
                break

        return now.getValue()[0]

    def printTree(self):
        q = deque()
        # 노드, layer, 위치
        q.append((self.root, 0, "C"))

        while q:
            node, layer, position = q.popleft()
            print(node.getValue(), layer, position)

            leftChild = node.getLeftChild()
            rightChild = node.getRightChild()

            if leftChild != None:
                q.append((leftChild, layer + 1, position + "L"))
            if rightChild != None:
                q.append((rightChild, layer + 1, position + "R"))



for _ in range(loop):
    
    tree = Tree()
    case = int(input())
    
    for g in range(case):
        op, number = input().split()
        number = int(number)

        if op == "I":
            tree.insert(number)
        elif op == "D":
            if number == 1:
                tree.deleteBiggest()
            elif number == -1:
                tree.deleteSmallest()

        # tree.printTree()

    if tree.root.getValue()[1] == 0:
        print("EMPTY")
    else:
        print(tree.getBiggestValue(), tree.getSmallestValue())