# +---------------------------------------------------------------------------+
# |              Etch-A-Whiteboard instruction file generator                 |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import sys
from copy import deepcopy

##################################START OF PROGRAM#############################
#======================< GLOBAL STUFFS >===========Instruction File Generator==
WIDTH = 0
HEIGHT = 0
idealTotalVertSteps = 15555
pixScale = 21 # NOTE: will have to change based on image size
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
#--------------------------------------------------Instruction File Generator--
def input(filename):
    global WIDTH, HEIGHT
    txt = open ( filename ) . read() . split()

    txt.pop(0)
    nextthing = txt.pop(0)
    while not isInt(nextthing):
        nextthing = txt.pop(0)

    WIDTH = int(nextthing)
    HEIGHT = int(txt.pop(0))
    maxRGB = txt.pop(0)

    img = [[1 if int(txt[(row*WIDTH + col)*3]) >= 250 else 0 for col in range( WIDTH )] for row in range(HEIGHT)]

    return img
#--------------------------------------------------Instruction File Generator--
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
#--------------------------------------------------Instruction File Generator--
def outputImage(filename, img):
    outfile  = open ( filename , 'w' )
    outfile.write('P3\n' + str(WIDTH) + ' ' + str( HEIGHT ) + '\n255\n')
    for row in range (HEIGHT):
        for col in range (WIDTH):
            val = '255' if img[row][col] else '0'
            outfile.write(val + ' ' + val + ' ' + val + ' ')
    outfile.close()
#--------------------------------------------------Instruction File Generator--
def adjacentPixels(img, row, col, exclude = []):
    lst = []
    for (dr, dc) in DIRECTIONS:
        nr , nc = row + dr , col + dc
        if nr < 0 or nc < 0 or nr == HEIGHT or nc == WIDTH or (nr,nc) in exclude:
            continue
        if img[nr][nc]:
            lst.append((dr,dc))
    return lst
#--------------------------------------------------Instruction File Generator--
def followLineAndPrint(img, drawn, row, col, outfile): #erases from original as it goes, and adds to 'drawn'
    #perhaps keep track of last 8 and ignore those (so you can leave some in where there are forks)
    # note: can check if corner with boolean = adder[0] and adder[1]
    adj = adjacentPixels(img, row, col)
    while adj:
        dr , dc = 0, 0
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
#--------------------------------------------------Instruction File Generator--
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
#--------------------------------------------------Instruction File Generator--
def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            print (x, y)
            yield (x,y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
#===============================< MAIN >========================================
def main():
    filename = sys.argv[1]
    img = input(filename)
    #risky pixScale = idealTotalVertSteps // HEIGHT
    outfile = open(filename[:-4] + '.eaw', 'w')
    drawn = [[0 for col in range(WIDTH)] for row in range(HEIGHT)]

    #assume pen starts at 0,0
    pr = 0
    pc = 0

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if img[row][col]:
                print('it happened')
                moveWithPenUp(pr,pc,row,col, outfile)
                pr, pc = followLineAndPrint(img, drawn, row, col, outfile)
                #outputImage(filename[:-4] + str(count) + '.ppm', drawn) #for debugging
    '''            break;
        if pr != 0 or pc != 0:
            break;
    opr = 0
    opc = 0
    while opr != pr and opc != pc:
        for (dr , dc) in spiral(max(HEIGHT-pr, pr), max(WIDTH -pc, pc)):
            if 0 <= pr + dr < HEIGHT and 0 <= pc + dc < WIDTH and img[pr+dr][pc+dc]:
                                print('it happened')
                                moveWithPenUp(pr,pc,pr+dr,pc +dc, outfile)
                                pr, pc = followLineAndPrint(img, drawn, pr+dr, pc+dc, outfile)
                                break
        opr = pr
        opc = pc'''

    #outputImage("debug.ppm",drawn)

    outfile.close()
#--------------------------------------------------Instruction File Generator--
if __name__ == '__main__': from time import clock; START_TIME = clock();  main(); \
                           print('--> Run time =', round(clock() - START_TIME, 2), 'seconds <--');
#############################< END OF PROGRAM >#################################