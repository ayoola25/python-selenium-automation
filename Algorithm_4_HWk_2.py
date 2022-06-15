# Increment a Number
# Write a program that takes as input an array of digits encoding a non-negative decimal integer D
# and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment(a):
    n = len(a)

    a[n - 1] += 1
    carry = a[n - 1] / 10
    a[n - 1] = a[n - 1] % 10

    for i in range(n - 2, -1, -1):
        if (carry == 1):
            a[i] += 1
            carry = a[i] / 10
            a[i] = a[i] % 10

    if (carry == 1):
        a.insert(0, 1)

numb = [1, 2, 9]

increment(numb)

for i in range(0, len(numb)):
    print(numb[i], end=" ")