import collections
import math as m
import sys
from collections import deque

class Node:
    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent

def getNeighbors(matrix, x, y):
    neighbors = []

    if y >= 0 and y < len(matrix[x]) - 1:
        node = Node(matrix[x][y+1], matrix[x][y])
        neighbors.append(node)


    if y >= 1 and y < len(matrix[x]):
        node = Node(matrix[x][y-1], matrix[x][y])
        neighbors.append(node)
        #neighbors.append(matrix[x][y-1])
    
    if x >= 1 and x < len(matrix):
        #node = Node(matrix[x][y+1], matrix[x][y])
        #neighbors.append(matrix[x+1][y])
        node = Node(matrix[x+1][y], matrix[x][y])
        neighbors.append(node)

    if x >= 2 and x <= len(matrix):
        #node = Node(matrix[x][y+1], matrix[x][y])
        #neighbors.append(matrix[x-1][y])

        node = Node(matrix[x-1][y], matrix[x][y])
        neighbors.append(node)
    
    return neighbors


def bfs(node,goal,size,grid):
    queue = deque()
    queue.append(node)
    explored.append(node.point)
    while queue:
        t = queue.popleft()
        if t.point not in explored:
            explored.append(t.point)
        if t.point == goal:
            return t
        for child in children(t.point,size,grid):
            if child not in explored:
                u = Node(child,t)
                queue.append(u)
    return None
# Tail starts here
'''
def bfs(graph, start, end):
    print 'bfs'
    visited, queue = set(), [start]
    counter = 0
    nodes = []
    while queue:
        #print queue
        #for i in queue:
            #print i,
        node = queue.pop(0)
        
        counter += 1
        print node.point, start.point, end.point
        if node.point == end.point:
            
            return node

        elif node.point not in visited and node.point not in queue:
            visited.add(node.point)

            for n in graph[node.point]:
                if node.point != '*':
                    if n.point not in visited:
                        queue.append(n)
            

    return None
'''
def children(point,size,grid):
    print point
    x,y = point
    size_x, size_y = size
    children = [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]
    return [child for child in children if grid[child[0]][child[1]] != '%']

def createGraph(matrix):
    graph = {}
    enter = []
    nodes = {}
    for i in range(1, len(matrix) + 1):
        for j in range(0, len(matrix[i])):
            print matrix[i][j]
            node = Node(matrix[i][j], None)
            graph[node.point] = None
            if matrix[i][j] == '*':
                if graph[node.point] != None:
                    graph[node.point] = graph[node.point] + getNeighbors(matrix, i, j)
                else:
                    graph[node.point] = getNeighbors(matrix, i, j)
            else:
                graph[node.point] = getNeighbors(matrix, i, j)

    return graph
explored = []
def keyboarding(rows, columns, matrix, word):
    graph = createGraph(matrix)
    print graph

    print matrix
    pos = 0
    last_v = Node(matrix[1][0])
    while pos < len(word) - 1:
        #def bfs(node,goal,size,grid):
        #node = Node((pacman_x, pacman_y))
        node = bfs(last_v, Node(word[pos]),(rows,columns),matrix)

        #node = bfs(graph, last_v, Node(word[pos], None))
        if node != None:
            
            path = []
            while node != None:
                print node
                path.append(node.point)
                node = node.parent
            path.reverse()
            
        last_v = Node(word[pos])
        print
        pos+=1

    print 'stuif'
    bfs(graph, last_v, Node('*', None))
	
matrix = {}
while True:
    #try:

    rows, columns = map(int, raw_input().strip().split(' '))
    for i in range(1, rows + 1):
        matrix[i] = list(raw_input().strip())
        #print matrix[i]
    word = list(raw_input().strip())

    print keyboarding(rows, columns, matrix, word)
    #except:
        #e = sys.exc_info()[0]
        #print(e)
        #break




