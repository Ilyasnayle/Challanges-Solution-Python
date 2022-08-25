def BitwiseOne(strArr):

  # code goes here
  answer = ""

  for i in range(0, len(strArr[0])):
    if strArr[0][i] == "0" and strArr[1][i]=="0":
      answer += "0"
    else:
      answer +="1"
  return answer

# keep this function call here 
print(BitwiseOne(input()))
