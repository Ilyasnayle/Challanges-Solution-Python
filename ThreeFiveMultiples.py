def ThreeFiveMultiples(num):

  # code goes here
  answer = []

  for i in range(num):
    if (i%3 == 0 or i%5 ==0):
      answer.append(i)

  return sum(answer)


# keep this function call here 
print(ThreeFiveMultiples(input()))
