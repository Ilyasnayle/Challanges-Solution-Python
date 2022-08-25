def Fibonaci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
Fibonaci(int(input('Please input a number: ')))
