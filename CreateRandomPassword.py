def CreateRandomPassword(n):
    import random
    password = ''
    for i in range(n):
        password += chr(random.randint(48, 122))
    return password
print(CreateRandomPassword(int(input('Please input a number: '))))
