
#Palindrome Two

#Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome,
#(the string is the same forward as it is backward) otherwise return the string false. The parameter entered may have punctuation and symbols 
#but they should not affect whether the string is in fact a palindrome. For example:
#"Anne, I vote more cars race Rome-to-Vienna" should return true.


def palindrome(a):
  x = ''

  for c in a.lower():
    cx = ''
    if c>= '0' and c<= '9':
      cx = c
    elif c >= 'a' and c<='z':
      cx = c
      x = cx + x
  return x

def PalindromeTwo(strParam):

  # code goes here
  a = palindrome(strParam)
  if a == a[::-1]:
    return 'true'
  return 'false'



# keep this function call here 
print(PalindromeTwo(input()))
