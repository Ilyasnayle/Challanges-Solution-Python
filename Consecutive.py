def Consecutive(arr):

  # code goes here

  sort = sorted(arr)
  add = 0

  for i in range(len(arr) -1 ):
    add = add + sort[i+1] - sort[i] - 1

  return add

# keep this function call here 
print(Consecutive(input()))
