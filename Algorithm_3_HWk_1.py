# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def meanOfList(numOfList):
    mean = sum(numOfList) / len(numOfList)
    return mean

print("The arithmetical mean is", round(meanOfList([1, 3, 5, 6, 4, 10, 2, 3]), 2))