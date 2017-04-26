import collections
import math as m
import sys
from collections import deque

class Node:
    def __init__(self, point, parent=None, position=None):
        self.point = point
        self.parent = parent
        self.position = position


def bfs(node, start, goal, grid, x, y):
    queue = deque()
    queue.append(node)
    explored = []
    explored.append(node.position)
    while queue:
        node = queue.popleft()
        if node.position not in explored:
            explored.append(node.position)

        if node.point == goal:
            return node

        for x, y in children(grid, node.position[0], node.position[1]):
            if (x,y) not in explored:
                u = Node(grid[x][y], node, (x, y))
                queue.append(u)
    return None

def children(matrix, x, y):
    size_x = len(matrix)
    size_y = len(matrix[1])
    children = [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]
    return [child for child in children if (child[0] >= 0 and child[1] >= 0) and (child[0] < size_x and child[1] < size_y)]

def getPath(node):
    path = []
    while node != None:
        path.append(node)
        node = node.parent
    return path

def keyboarding(rows, columns, matrix, word):
    pos = 0
    start = Node(matrix[0][0], None, (0, 0))
    counter = 0
    while pos < len(word):

        node = bfs(start, start, word[pos], matrix, start.position[0], start.position[1])
        if node != None:
            path = getPath(node)
            counter += len(path)
            start = Node(word[pos], None, path[0].position)
        pos+=1

    start = Node(node.point, None, path[0].position)
    node = bfs(start, start, '*', matrix, start.position[0], start.position[1])
    path = getPath(node)
    counter += len(path)
    return counter
	
matrix = {}
while True:
    #try:

    rows, columns = map(int, raw_input().strip().split(' '))
    for i in range(0, rows):
        matrix[i] = list(raw_input().strip())
        #print matrix[i]
    word = list(raw_input().strip())

    print keyboarding(rows, columns, matrix, word)
    #except:
        #e = sys.exc_info()[0]
        #print(e)
        #break




