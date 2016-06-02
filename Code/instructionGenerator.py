# +---------------------------------------------------------------------------+
# |              Etch-A-Whiteboard instruction file generator                 |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import sys
from copy import deepcopy

##################################START OF PROGRAM#############################
#======================< GLOBAL STUFFS >==========================Class Name==
#BOARD_WIDTH = 
#BOARD_HEIGHT = 
WIDTH = 0
HEIGHT = 0
pixScale = 5
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
#-----------------------------------------------------------------Class Name--
def input(filename):
    global WIDTH, HEIGHT
    txt = open ( filename ) . read() . split()

    txt.pop(0)

    WIDTH = int(txt.pop(0))
    HEIGHT = int(txt.pop(0))
    maxRGB = txt.pop(0)

    img = [[1 if int(txt[(row*WIDTH + col)*3]) >= 250 else 0 for col in range( WIDTH )] for row in range(HEIGHT)]

    return img
#-----------------------------------------------------------------Class Name--
def outputImage(filename, img):
    outfile  = open ( filename , 'w' )
    outfile.write('P3\n' + str(WIDTH) + ' ' + str( HEIGHT ) + '\n255\n')
    for row in range (HEIGHT):
        for col in range (WIDTH):
            val = '255' if img[row][col] else '0'
            outfile.write(val + ' ' + val + ' ' + val + ' ')
    outfile.close()
#-----------------------------------------------------------------Class Name--
def adjacentPixels(img, row, col, exclude = []):
    lst = []
    for (dr, dc) in DIRECTIONS:
        nr , nc = row + dr , col + dc
        if nr < 0 or nc < 0 or nr == HEIGHT or nc == WIDTH or (nr,nc) in exclude:
            continue
        if img[nr][nc]:
            lst.append((dr,dc))
    return lst
#-----------------------------------------------------------------Class Name--
def followLineAndPrint(img, drawn, row, col, outfile): #erases from original as it goes, and adds to 'drawn'
    #perhaps keep track of last 8 and ignore those (so you can leave some in where there are forks)
    # note: can check if corner with boolean = adder[0] and adder[1]
    adj = adjacentPixels(img, row, col)
    while adj:
        dr , dc = 0, 0
        if len(adj) > 1:
            # have to choose where to go
            for d in adj:
                if not (d[0] and d[1]):
                    (dr, dc) = d
                    break
        if not (dr or dc):
            (dr, dc) = adj[0]
        outfile.write(str(DIRECTIONS.index((dr,dc))) + ' ' + str(pixScale) + '\n')
        img[row][col] = 0
        drawn[row][col] = 1
        row += dr
        col += dc
        #prep for next time
        adj = adjacentPixels(img, row, col)
    img[row][col] = 0
    drawn[row][col] = 1
    return row, col 
#-----------------------------------------------------------------Class Name--
def moveWithPenUp(r1, c1, r2, c2, outfile):
    #put pen up
    outfile.write('8 1\n')
    #move
    dirx = 2 if c2 > c1 else 6
    diry = 0 if r2 < r1 else 4
    outfile.write(str(dirx) + ' ' + str(pixScale * max(c1-c2,c2-c1)) + '\n')
    outfile.write(str(diry) + ' ' + str(pixScale * max(r1-r2,r2-r1)) + '\n')
    #put pen down
    outfile.write('9 1\n')
#===============================< MAIN >========================================
def main():
    filename = sys.argv[1]
    img = input(filename)
    #pixScale = min(BOARD_WIDTH/ WIDTH, BOARD_HEIGHT / HEIGHT)
    outfile = open(filename[:-4] + '.eaw', 'w')
    drawn = [[0 for col in range(WIDTH)] for row in range(HEIGHT)]

    #assume pen starts at 0,0
    pr = 0
    pc = 0

    count = 0
    for row in range(WIDTH):
        for col in range(HEIGHT):
            if img[row][col]:
                print('it happened')
                moveWithPenUp(pr,pc,row,col, outfile)
                pr, pc = followLineAndPrint(img, drawn, row, col, outfile)
                outputImage(filename[:-4] + str(count) + '.ppm', drawn)
                count += 1

    outfile.close()
#-----------------------------------------------------------------Class Name--
if __name__ == '__main__': from time import clock; START_TIME = clock();  main(); \
                           print('--> Run time =', round(clock() - START_TIME, 2), 'seconds <--');
#############################< END OF PROGRAM >#################################
