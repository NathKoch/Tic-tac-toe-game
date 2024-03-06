# Play tic-tac-toe game against computer.

>**Tic-tac-toe** or **noughts and crosses** 
is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O.
 The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

The board should be implemented using nested lists.   
 This is an example of the board:
 ```python
  column   
  1  2  3   
[ ][ ][ ]  row 1   
[ ][ ][ ]  row 2   
[ ][ ][ ]  row 3  
```

- To create a movement you need to type the first value for the `row(1-3)` then click **Enter** and then type the value for the `column(1-3)` and click **Enter**.  
- The program moves after you and your moves and the program’s moves are immediately displayed.
```
Left 9 moves
Select a row (1-3)2
Select a column (1-3)3
Your move:
[ ][ ][ ]
[ ][ ][X]
[ ][ ][ ]
Program move:
[ ][ ][0]
[ ][ ][X]
[ ][ ][ ]
Left 7 moves
Select a row (1-3)
```
Function `testForFreeCell()` display how many free moves are left.
If there are no free cells, it will be a draw.
```python
def testForFreeCell():
  
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
```
Game tactics of the program **"Random selection"**, this leaves room for improvement in program tactics.