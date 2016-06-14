#!/usr/bin/env python2

import sys

def middle(data, start, end, compare) :
    left = start
    right = end

    flag = data[end]
    
    turn = 0   # left turn : 0
               # right turn: 1

    while left < right :
        if turn == 0 :
            if compare(data[left], flag) :
                data[right] = data[left]
                turn = 1
            else :
                left += 1
        else :
            if not compare(data[right], flag) :
                data[left] = data[right]
                turn = 0
            else :
                right -= 1

    data[left] = flag

    return left

def quicksort(data, start, end, compare):
    if start >= end :
        return

    m = middle(data, start, end, compare)
    quicksort(data, start, m - 1, compare)
    quicksort(data, m + 1, end, compare)

def main(data) :
    quicksort(data, 0, len(data) - 1, lambda a, b : True if a > b else False)
    print data

if __name__ == '__main__' :
    if len(sys.argv) != 2 :
        print 'error input param, input len is %d' % (len(sys.argv) - 1)
        exit(-1)
    data_str = sys.argv[1].split(',')
    data = []
    for s in data_str :
        try :
            data.append(int(s))
        except ValueError, e :
            print 'error input param, input param is %s' %(sys.argv[1])
            exit(-2)

    main(data)
