def MaximalSquare(strParam):

  # code goes here

  List = list([[int(x) for x in s ] for s in strParam])

  Row = len(strParam)
  Col = len(strParam[0])

  F = min(Row , Col)

  for f in range(F, 0 , -1):

    for i in range(0 , Row - f + 1):

      for j in range(0, Col - f + 1):

        mul = 1

        for a in range( i, f+i):

          for b in range(j, f+j):

            mul = mul * List[a][b]

        if mul == 1:

          return f * f
  return 0

# keep this function call here 
print(MaximalSquare(input()))
