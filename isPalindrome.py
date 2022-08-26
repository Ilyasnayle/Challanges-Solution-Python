
def Reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = Reverse(s)
    if (s == rev):
        return True
    return False
  
def main():
    s = input("Enter a string: ")
    if (isPalindrome(s)):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
