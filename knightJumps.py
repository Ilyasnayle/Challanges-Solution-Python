## Knight Jumps

#Have the function KnightJumps(str) read str which will be a string consisting of the location of a knight on a standard 8x8 chess board with no other pieces on the board. 
#The structure of str will be the following: "(x y)" which represents the position of the knight with x and y ranging from 1 to 8. 
#Your program should determine the number of spaces the knight can move to from a given location. For example:
#if str is "(4 5)" then your program should output 8 because the knight can move to 8 different spaces from position x=4 and y=5.

 
chessboardMoves = [
  [2,3,4,4,4,4,3,2],
  [3,4,6,6,6,6,4,3],
  [4,6,8,8,8,8,6,4],
  [4,6,8,8,8,8,6,4],
  [4,6,8,8,8,8,6,4],
  [4,6,8,8,8,8,6,4],
  [3,4,6,6,6,6,4,3],
  [2,3,4,4,4,4,3,2]
] 

def KnightJumps(strParam):

  # code goes here
  x , y = strParam.replace("(", "").replace(")", "").split(" ")
  return chessboardMoves[int(x)-1][int(y)-1]


# keep this function call here 
print(KnightJumps(input()))
