#笔试答案说明#

##第一题.排序##

利用python进行开发，代码文件为test0.py，算法利用了快速排序，运行命令如:

python test0.py 5,4,3,6,7,1,8,2,9

最终输出从小到大的排列顺序

[1, 2, 3, 4, 5, 6, 7, 8, 9]

##第二题.数字输出##

利用python进行开发，代码文件为test1.py，运行命令如下

python test1.py 3 7638

最终将格式化输出

     ---  ---  ---  --- 
        ||        ||   |
        ||        ||   |
        ||        ||   |
          ---  ---  --- 
        ||   |    ||   |
        ||   |    ||   |
        ||   |    ||   |
          ---  ---  --- 

##第三题.游戏开发##

###抱歉声明###

由于在加班时间做题，并且由于未进行过游戏开发，缺少资源，因此没有将该题完整的完成，只选择寻路算法进行开发

###说明###

利用python进行开发，代码文件为test2.py，地图已预置于代码中，利用A*算法进行最短寻路，其中地图的S位置为起始点，E位置为终点，#为障碍物，输出中星号为路径标识，运行命令如下

python test2.py

最终将格式化输出:

    ############################################################
    #..........................................................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #.......S.....................#............................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #.............................#............................#
    #######.#######################################............#
    #....#........#............................................#
    #....#........#............................................#
    #....##########............................................#
    #..........................................................#
    #..........................................................#
    #..........................................................#
    #..........................................................#
    #..........................................................#
    #...............................##############.............#
    #...............................#........E...#.............#
    #...............................#............#.............#
    #...............................#............#.............#
    #...............................#............#.............#
    #...............................###########..#.............#
    #..........................................................#
    #..........................................................#
    ############################################################

    ----------------------------------------------------------------------------------------------------

    ############################################################
    #.............................**...........................#
    #............................*#*...........................#
    #...........................*.#*...........................#
    #..........................*..#*...........................#
    #.......*******************...#*...........................#
    #.............................#*...........................#
    #.............................#*...........................#
    #.............................#*...........................#
    #.............................#*...........................#
    #.............................#*...........................#
    #.............................#*...........................#
    #.............................#*****************...........#
    #######.#######################################*...........#
    #....#........#...............................*............#
    #....#........#...............................*............#
    #....##########...............................*............#
    #.............................................*............#
    #.............................................*............#
    #.............................................*............#
    #.............................................*............#
    #.............................................*............#
    #...............................##############*............#
    #...............................#........*...#*............#
    #...............................#........*...#*............#
    #...............................#.........*..#*............#
    #...............................#..........*.#*............#
    #...............................###########.*#*............#
    #............................................*.............#
    #..........................................................#
    ############################################################

    ----------------------------------------------------------------------------------------------------

***fix***:重做第三题，使用Astah工具画类图，原始文件为test2.asta，导出图片为test2.png
