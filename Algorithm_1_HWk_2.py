#Find max number from 3 values, entered manually from a keyboard.

def numMax(x, y, z):
    if x >y and x > z:
        return x
    if y >x and y > z:
        return y
    else:
        return z

num1 = int(input('Input Number: '))
num2 = int(input('Input Number: '))
num3 = int(input('Input Number: '))

print(numMax(num1, num2, num3))