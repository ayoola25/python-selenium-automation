# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’

s = "bbbbbcaaaaa"
s1 = s[:len(s)//2 if len(s)%2 == 0
                     else (((len(s)//2))+1):]
s2 = s[len(s)//2 if len(s)%2 == 0
                     else (((len(s)//2))+1):]

print(s1,s2)
print(s2 + s1)