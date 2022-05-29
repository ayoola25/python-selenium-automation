#Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n

def digSum(n):
    total_sum = 0
    for x in range(n + 1):
        total_sum = total_sum + x
    return total_sum

number = int(input('Input Number Here: '))
print(digSum(number))


