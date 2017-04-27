import collections
import math as m
import sys
from collections import deque

class Node:
    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent



repeated = 0

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
            if node.point != grid[x][y] and (x,y) not in explored:
                u = Node(grid[x][y], node, (x, y))
                queue.append(u)
    return None

def children(matrix, x, y, row, col):
    #children = [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]
    # cc = []
    # for c in children:
    #     if (child[0] >= 0 and child[1] >= 0) and (child[0] < size_x and child[1] < size_y):
    #         if 
    #         cc.append(c)
    childs = []
    if x - 1 >= 0:
        if matrix[x][y] != matrix[x-1][y]:
            childs.append((x-1, y))
        else:
            inc=x-1
            while inc >= 0:
                if matrix[x][y] == matrix[inc][y] and inc < row-1:
                    inc-=1
                    continue
                childs.append((inc, y))
                childs.append((inc, y))
                break

    if x + 1 < row:
        if matrix[x][y] != matrix[x+1][y]:
            childs.append((x+1, y))
        else:
            inc = x + 1
            while inc < row:
                if matrix[x][y] == matrix[inc][y] and inc < row-1:
                    inc += 1
                    continue
                childs.append((inc, y))
                childs.append((inc, y))
                break

    if y - 1 >= 0:
        if matrix[x][y] != matrix[x][y-1]:
            childs.append((x, y-1))
        else:
            inc = y - 1
            while inc >= 0:
                if matrix[x][y] == matrix[x][inc] and inc < col-1:
                    inc-=1
                    continue
                childs.append((x, inc))
                childs.append((x, inc))
                break

    if y + 1 < col:
        if matrix[x][y] != matrix[x][y+1]:
            childs.append((x, y+1))
        else:
            inc = y + 1
            while inc < col:
                if matrix[x][y] == matrix[x][inc] and inc < col-1:
                    inc += 1
                    continue
                childs.append((x, inc))
                childs.append((x, inc))
                break

    return childs

def getPath(node):
    path = []
    pathc = []
    while node != None:
        path.append(node)
        print node.point
        node = node.parent

    return path

def createGraph(matrix, row, col):
    graph = {}
    for i in range(0, row):
        for j in range(0, col):
            childs = []
            childs = children(matrix, i, j, row, col)
            graph[(i,j)] = childs

    return graph

def bfsGraph(matrix, graph, start, goal):
    global repeated
    print 'bfsGraph'
    print start.point
    print goal
    queue = deque()
    queue.append(start)
    explored = []
    explored.append(start.point)
    while queue:
        node = queue.popleft()
        if node.point not in explored:
            explored.append(node.point)

        print node.point
        if matrix[node.point[0]][node.point[1]] == goal:
            print 'goal'
            print goal
            return node

        last = None
        repeats = {}
        for x, y in graph[node.point]:
            #print x,y
            if (x, y) in repeats:
                repeats[(x, y)] += 1
            else:
                repeats[(x, y)] = 1
            
            if node.point != (x, y) and (x,y) not in explored:
                u = Node((x, y), node)
                queue.append(u)

            last = (x, y)




        print 'repeats'
        print (repeats)
        for i in repeats:
            print repeats[i]
            print
            if repeats[i] > 2:
                repeated += 1
    return 0

def keyboarding(rows, columns, matrix, word):
    graph = createGraph(matrix, rows, columns)
    print graph
    '''
    print graph
    print 'graph'
    for g in graph:
        print g
        print matrix[g[0]][g[1]]

        for a in graph[(g[0], g[1])]:
            print matrix[a[0]][a[1]],

        print

    '''
    
    pos = 0
    start = Node((0, 0), None)
    counter = 0
    while pos < len(word):
        node = bfsGraph(matrix, graph, start, word[pos])

        #node = bfs(start, start, word[pos], graph, start.position[0], start.position[1])
        if node != None:
            
            path = getPath(node)
            counter += len(path)
            #print path
            start = Node(path[0].point, None)
        pos+=1

    start = Node(node.point, None)
    #node = bfs(start, start, '*', matrix, start.position[0], start.position[1])
    node = bfsGraph(matrix, graph, start, '*')
    path = getPath(node)
    counter += len(path) + repeated
    
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




