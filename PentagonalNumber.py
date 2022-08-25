def PentagonalNumber(num):

  # code goes here

  if num == 1:
    return 1
  else:
    return (num -1 ) * 5 + PentagonalNumber(num -1)
  

# keep this function call here 
print(PentagonalNumber(input()))
