from random import randint
field=[[' ',' ',' '], # field[0]
       [' ',' ',' '], # field[1]
       [' ',' ',' ']] # field[2]
def testForWinner():
    winner=False
    # first row check 
    if field[0][0]==field[0][1] and field[0][1]==field[0][2] and field[0][0]!=' ':
        winner=True
    # second row check 
    if field[1][0]==field[1][1] and field[1][1]==field[1][2] and field[1][0]!=' ':
        winner=True        
    # third row check 
    if field[2][0]==field[2][1] and field[2][1]==field[2][2] and field[2][0]!=' ':
        winner=True
    # first column check 
    if field[0][0]==field[1][0] and field[1][0]==field[2][0] and field[0][0]!=' ':
        winner=True
    # second column check 
    if field[0][1]==field[1][1] and field[1][1]==field[2][1] and field[0][1]!=' ':
        winner=True
    # third column check 
    if field[0][2]==field[1][2] and field[1][2]==field[2][2] and field[0][2]!=' ':
        winner=True
    # downward diagonal check 
    if field[0][0]==field[1][1] and field[1][1]==field[2][2] and field[0][0]!=' ':
        winner=True
    # upward diagonal check 
    if field[2][0]==field[1][1] and field[1][1]==field[0][2] and field[2][0]!=' ':
        winner=True
    return winner

 
def testForFreeCell():
    # ==========================================
    # counting empty cells on the playing field
    # ==========================================
    empty=0
    for i in range(0,3):
        for j in range(0,3):
            if field[i][j]==' ':
                empty+=1
    return empty
while True:
    if testForFreeCell()==0:
        print("Draw")
        break
    #=========================================
    #========================================
    print("Left",testForFreeCell(),"moves")
    r=input("Select a row (1-3)")
    c=input("Select a column (1-3)")
    if (int(r) < 4 and int(c) < 4 and int(r) > 0 and int(c) > 0):
        field[int(r)-1][int(c)-1]="X"
    else:
        print('Invalid cell number entered! Please try again!')
        break 
    # field[int(r)-1][int(c)-1]="X"
    print('Your move:')
    print('['+field[0][0]+']['+field[0][1]+']['+field[0][2]+']')
    print('['+field[1][0]+']['+field[1][1]+']['+field[1][2]+']')
    print('['+field[2][0]+']['+field[2][1]+']['+field[2][2]+']')
    if testForWinner()==True:
        print("You won!")
        break
    if testForFreeCell()==0:
        print("Draw")
        break
    # game tactics of the program "Random selection"
    while True:
        nR=randint(0,2)
        nC=randint(0,2)
        if field[nR][nC]==' ':
            break # if it finds an empty cell, it exits the repeat loop
    field[nR][nC]='0'
    print('Program move:')
    print('['+field[0][0]+']['+field[0][1]+']['+field[0][2]+']')
    print('['+field[1][0]+']['+field[1][1]+']['+field[1][2]+']')
    print('['+field[2][0]+']['+field[2][1]+']['+field[2][2]+']')
    if testForWinner()==True:
        print("We believe that next time you will do even better!")
        break
