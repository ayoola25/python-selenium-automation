# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

ip = [198, 3, 4, 9, 10, 9, 2]

first, second = ip[0], ip[0]
for num in ip[1:]:
    if num < first:
        second = first
        first = num

print(first, second)