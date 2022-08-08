import sys
from collections import deque

input = sys.stdin.readline

loop = int(input())

DEFAULT = int(1e9)

class Node:
    def __init__(self, value = DEFAULT) -> None:
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def setValue(self, value = DEFAULT):
        if value == DEFAULT:
            self = None
        else:
            self.__value = value

    def getValue(self):
        return self.__value

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, value = DEFAULT):
        if value == DEFAULT:
            self.__leftChild = None
        else:
            self.__leftChild = Node(value)

    def setRightChild(self, value = DEFAULT):
        if value == DEFAULT:
            self.__rightChild = None
        else:
            self.__rightChild = Node(value)

    def isLeafNode(self):
        return self.getLeftChild() == None and self.getRightChild() == None
            
class Tree:
    def __init__(self) -> None:
        self.root = Node(DEFAULT)
        self.biggestNodePointer = self.root
    
    def insert(self, value):
        presentNode = self.root

        while presentNode != None:
            presentNodeValue = presentNode.getValue()

            if presentNodeValue == DEFAULT:
                presentNode.setValue(value)
                return
            else:
                leftChild = presentNode.getLeftChild()
                rightChild = presentNode.getRightChild()
                if presentNodeValue > value:
                    presentNode.setValue(value)
                    value = presentNodeValue

                    if leftChild == None:
                        presentNode.setLeftChild(presentNodeValue)
                        return
                    elif rightChild == None:
                        presentNode.setRightChild(presentNodeValue)
                        return
                    else:
                        presentNode = leftChild if leftChild.getValue() < rightChild.getValue() else rightChild
                else:
                    if leftChild == None:
                        presentNode.setLeftChild(value)
                        return
                    elif rightChild == None:
                        presentNode.setRightChild(value)
                        return
                    else:
                        presentNode = leftChild if leftChild.getValue() < rightChild.getValue() else rightChild

                        
    def deleteBiggest(self):
        biggestNode, parentNode = self.__getBiggestNode()
        if parentNode.getLeftChild() is biggestNode:
            parentNode.setLeftChild(DEFAULT)
        elif parentNode.getRightChild() is biggestNode:
            parentNode.setRightChild(DEFAULT)
        else:
            self.root = Node()

    def deleteSmallest(self):
        biggestNode, parentNode = self.__getBiggestNode()
        biggestValue = biggestNode.getValue()
        if parentNode.getLeftChild() is biggestNode:
            parentNode.setLeftChild(DEFAULT)
            self.root.setValue(biggestValue)
        elif parentNode.getRightChild() is biggestNode:
            parentNode.setRightChild(DEFAULT)
            self.root.setValue(biggestValue)
        elif self.root is biggestNode:
            self.root = Node()
            return

        presentNode = self.root

        while presentNode != None:
            leftChild = presentNode.getLeftChild()
            rightChild = presentNode.getRightChild()
            if leftChild == None and rightChild == None:
                return
            else:
                if leftChild != None and leftChild.getValue() < presentNode.getValue():
                    leftChildValue = leftChild.getValue()
                    leftChild.setValue(presentNode.getValue())
                    presentNode.setValue(leftChildValue)
                    presentNode = leftChild
                elif rightChild != None and rightChild.getValue() < presentNode.getValue():
                    rightChildValue = rightChild.getValue()
                    rightChild.setValue(presentNode.getValue())
                    presentNode.setValue(rightChildValue)
                    presentNode = rightChild
                else:
                    return

    def __getBiggestNode(self):
        presentNode = self.root
        parentNode = self.root
        while presentNode != None:
            if presentNode.isLeafNode():
                return [presentNode, parentNode]
            else:
                leftChild = presentNode.getLeftChild()
                rightChild = presentNode.getRightChild()

                if leftChild != None and rightChild == None:
                    parentNode = presentNode
                    presentNode = leftChild
                elif leftChild == None and rightChild != None:
                    parentNode = presentNode
                    presentNode = rightChild
                else:
                    parentNode = presentNode
                    presentNode = leftChild if leftChild.getValue() > rightChild.getValue() else rightChild
    
    def printTree(self):
        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            print(node.getValue())

            if node.getLeftChild() != None:
                q.append(node.getLeftChild())
            if node.getRightChild() != None:
                q.append(node.getRightChild())

    def getSmallestValue(self):
        return self.root.getValue()

    def getBiggestValue(self):
        biggestNode, _ = self.__getBiggestNode()
        return biggestNode.getValue()

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

    if tree.root.getValue() == DEFAULT:
        print("EMPTY")
    else:
        print(tree.getBiggestValue(), tree.getSmallestValue())