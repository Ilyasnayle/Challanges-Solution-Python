def SnakeCase(strParam):

  # code goes here

  list = []

  strParam2 = ""

  for i in strParam:
    if i.isalpha() and i != '':
      strParam2 = strParam2 + i
    else:
      strParam2 = strParam2.lower()
      list += [strParam2]
      strParam2 = ''
  
  strParam2 = strParam2.lower()
  list += [strParam2]
  strParam2 = '_'.join(list)

  return strParam2

# keep this function call here 
print(SnakeCase(input()))
