# https://www.acmicpc.net/problem/1991

# 링크드 리스트로 트리를 만든 후 순회한다.

class Node(object):
    name = ""
    left = None
    right = None
    def __init__(self, nodeName =".", left = None, right = None):
        if nodeName == ".":
            return None
        self.name = nodeName
        self.left = left
        self.right = right

nodes = {"A": Node("A") }
n = int(input())
for i in range(0, n):
    nodeNames = input().split(" ")

    nodes[nodeNames[1]] = Node(nodeNames[1])
    nodes[nodeNames[2]] = Node(nodeNames[2])

    nodes[nodeNames[0]].left = nodes[nodeNames[1]]
    nodes[nodeNames[0]].right = nodes[nodeNames[2]]

def preOrder(Node):
    if (Node == None): return
    print(Node.name, end="")
    preOrder(Node.left)
    preOrder(Node.right)

def mOrder(Node):
    if (Node == None): return
    mOrder(Node.left)
    print(Node.name, end="")
    mOrder(Node.right)

def postOrder(Node):
    if (Node == None): return
    postOrder(Node.left)
    postOrder(Node.right)
    print(Node.name, end="")

preOrder(nodes["A"])
print()
mOrder(nodes["A"])
print()
postOrder(nodes["A"])





