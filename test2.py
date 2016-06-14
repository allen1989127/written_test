#!/usr/bin/env python

import math

map = [
        '############################################################',
        '#..........................................................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.......S.....................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#.............................#............................#',
        '#######.#######################################............#',
        '#....#........#............................................#',
        '#....#........#............................................#',
        '#....##########............................................#',
        '#..........................................................#',
        '#..........................................................#',
        '#..........................................................#',
        '#..........................................................#',
        '#..........................................................#',
        '#...............................##############.............#',
        '#...............................#........E...#.............#',
        '#...............................#............#.............#',
        '#...............................#............#.............#',
        '#...............................#............#.............#',
        '#...............................###########..#.............#',
        '#..........................................................#',
        '#..........................................................#',
        '############################################################',
        ]

real_map = []

class Node :
    def __init__(self, parent, x, y, dist) :
        self.parent = parent
        self.x = x
        self.y = y
        self.dist = dist

'''
A Star
'''
class AstarAlgo :

    def __init__(self, startx, starty, endx, endy, width = 59, height = 30):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy

        self.width = width
        self.height = height

        self.open = []
        self.close = []
        self.path = []

    def legal(self, x, y) :
        if x < 0 or x > self.width or y < 0 or y > self.height :
            return False

        return real_map[y][x] != '#'

    def cost(self, x, y) :
        if math.fabs(x) == math.fabs(y) :
            return 1.41

        return 1.0

    def inList(self, node, l) :
        for i,n in enumerate(l) :
            if node.x == n.x and node.y == n.y :
                return i

        return -1

    def round(self, p):
        dxs = (-1, -1, -1,  0, 0,  1, 1,  1)
        dys = (-1,  0,  1, -1, 1, -1, 0, -1)

        dis = zip(dxs, dys)

        for dx, dy in dis :
            x, y = p.x + dx, p.y + dy
            if not self.legal(x, y) :
                continue

            node = Node(p, x, y, p.dist + self.cost(dx, dy))

            # if in close list
            if self.inList(node, self.close) != -1:
                continue

            index = self.inList(node, self.open)
            if index != -1 :
                if self.open[index].dist > node.dist :
                    self.open[index].parent = node.parent
                    self.open[index].dist = node.dist
                continue

            self.open.append(node)

    def getF(self, node) :
        return node.dist + math.sqrt(
                (self.endx - node.x) * (self.endx - node.x) + 
                (self.endy - node.y) * (self.endy - node.y)) * 1.2

    def getBestNode(self) :
        best = self.open[0]
        bestIndex = 0
        bestVal = self.getF(self.open[0])

        for i, node in enumerate(self.open) :
            val = self.getF(node)
            if val < bestVal :
                bestVal = val
                best = node
                bestIndex = i

        return bestIndex, best

    def isEnd(self, node) :
        return node.x == self.endx and node.y == self.endy

    def findPath(self):
        node = Node(None, self.startx, self.starty, 0.0)
        while True:
            self.round(node)
            if not self.open :
                return None

            index, node = self.getBestNode()
            if self.isEnd(node) :
                return node

            self.close.append(node)
            del self.open[index]

def make_map() :
    for line in map :
        real_map.append(list(line))

def find(tag) :
    x = -1
    y = -1
    for y, line in enumerate(real_map) :
        try :
            x = line.index(tag)
        except :
            continue
        else :
            break

    return x, y

def mark_path(node) :
    real_map[node.y][node.x] = '*'

def print_map() :
    for line in real_map :
        print ''.join(line)

    print
    print '-' * 100
    print

if __name__ == '__main__' :
    make_map()
    print_map()
    startx, starty = find('S')
    endx, endy = find('E')

    a_star = AstarAlgo(startx, starty, endx, endy)
    node = a_star.findPath()
    while node != None :
        mark_path(node)
        node = node.parent

    print_map()
