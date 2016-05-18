#encoding:utf8
#2_6棋盘覆盖.py
def ChessBoard(tr,tc,dr,dc,size):
    '''在一个(2**k)＊(2**k)个方格组成的棋盘，有一个方格为特殊方格，求棋盘覆盖问题'''
    #tr:左上角行号
    #tc:左上角列号
    #dr:特殊方格行号
    #dc:特殊方格列号
    #size:棋盘规格
    #tile:Ｌ型骨牌编号
    #Board:棋盘
    global Board
    global tile
    tile+=1
    t=tile
    if size==1:
        return
    halfSize=size//2
    #覆盖左上角棋盘
    if dr<tr+halfSize and dc<tc+halfSize:   #特殊方格在左上角棋盘中
        ChessBoard(tr,tc,dr,dc,halfSize)
    else:
        Board[tr+halfSize-1][tc+halfSize-1]=t    #用t号L型骨牌覆盖右下角
        ChessBoard(tr,tc,tr+halfSize,tc+halfSize,halfSize)

    #覆盖右上角棋盘
    if dr<tr+halfSize and dc>=tc+halfSize:
        ChessBoard(tr,tc+halfSize,dr,dc,halfSize)
    else:
        Board[tr+halfSize-1][tc+halfSize]=t
        ChessBoard(tr,tc+halfSize,tr+halfSize,tc+halfSize,halfSize)
    #覆盖左下角棋盘
    if dr>=tr+halfSize and dc<tc+halfSize:
        ChessBoard(tr+halfSize,tc,dr,dc,halfSize)
    else:
        Board[tr+halfSize][tc+halfSize-1]=t
        ChessBoard(tr+halfSize,tc,tr+halfSize,tc+halfSize-1,halfSize)
    #覆盖右下角棋盘
    if dr>=tr+halfSize and dc>=tc+halfSize:
        ChessBoard(tr+halfSize,tc+halfSize,dr,dc,halfSize)
    else:
        Board[tr+halfSize][tc+halfSize]=t
        ChessBoard(tr+halfSize,tc+halfSize,tr+halfSize,tc+halfSize,halfSize)

def show(Board):
    n=len(Board)
    for i in range(n):
        for j in range(n):
            print Board[i][j]
        print '\n'

tile=0
n=8
Board=[[-1 for x in range(n)] for y in range(n)]
ChessBoard(0,0,2,2,n)
show(Board)
