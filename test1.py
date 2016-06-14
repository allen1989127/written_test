#!/usr/bin/env python2

import sys

from abc import ABCMeta,abstractmethod

nums = {
        0 : [1, 1, 1, 0, 1, 1, 1],
        1 : [0, 1, 0, 0, 1, 0, 0],
        2 : [1, 0, 1, 1, 1, 0, 1],
        3 : [1, 0, 1, 1, 0, 1, 1],
        4 : [0, 1, 1, 1, 0, 1, 0],
        5 : [1, 1, 0, 1, 0, 1, 1],
        6 : [1, 1, 0, 1, 1, 1, 1],
        7 : [1, 0, 1, 0, 0, 1, 0],
        8 : [1, 1, 1, 1, 1, 1, 1],
        9 : [1, 1, 1, 1, 0, 1, 1],
        }

class DisplayFactory :
    @staticmethod
    def create(index, s) :
        dp = None

        # display - line
        if index == 0 :
            dp = HorDisplay(0)
        elif index == s + 1 :
            dp = HorDisplay(3)
        elif index == 2 * s + 2 :
            dp = HorDisplay(6)
        # display | line
        elif index > 0 and index < s + 1:
            dp = VerDisplay(1)
        else :
            dp = VerDisplay(4)

        return dp

class Display :
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self, s, n_list) :
        pass

class HorDisplay (Display):
    def __init__(self, index):
        self.index = index

    def display(self, s, n_list) :
        display_line = ''

        for i in range(len(n_list)) :
            if nums[n_list[i]][self.index] == 1 :
                display_line = display_line + ' ' + '-' * s + ' '
            else :
                display_line = display_line + ' ' + ' ' * s + ' '

        print display_line

class VerDisplay (Display):
    def __init__(self, index) :
        self.index = index

    def display(self, s, n_list) :
        display_line = ''

        for i in range(len(n_list)) :
            if nums[n_list[i]][self.index] == 1 :
                display_line = display_line + '|' + ' ' * s
            else :
                display_line = display_line + ' ' + ' ' * s

            if nums[n_list[i]][self.index + 1] == 1 :
                display_line = display_line + '|'
            else :
                display_line = display_line + ' '

        print display_line

def separate(n) :
    n_list = []
    while n / 10 > 0 :
        n_list.insert(0, n % 10)
        n /= 10

    n_list.insert(0, n)

    return n_list

def display_line(index, s, n_list) :
    dp = DisplayFactory.create(index, s)
    dp.display(s, n_list)

def display(s, n) :
    n_list = separate(n)
    
    columns = len(n_list) * (s + 2)
    rows = 2 * s + 3

    for i in range(rows) :
        display_line(i, s, n_list)

def main(argv) :
    if len(argv) != 3 :
        print 'error input with error argv, input with %d argv' % (len(argv) - 1)
        exit(-1)

    try :
        s = int(argv[1])
        n = int(argv[2])
        if s < 1 or s > 10 or n < 0 or n > 99999999:
            print 'error input num : s is %d, n is %d' % (s, n)
            exit(-2)

        display(s, n)
    except ValueError, e :
        print 'error input argv, input with %s and %s' % (argv[1], argv[2])
        exit(-3)

if __name__ == '__main__' :
    main(sys.argv)
