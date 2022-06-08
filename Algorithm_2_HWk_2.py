# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

myList = ['a','b','c','d','e']
def isUnique(list):
    x = []
    for i in list:
        if i in x:
            print(i)
            return False
        else:
            x.append(i)
    return True

print(isUnique(myList))