def count_hi(str):
    hellos = str.count('hello')
    his = str.count('hi')   
    return(hellos, his)

output1, output2 = count_hi('hi hello')
print(output1, output2)

'''
Q1: Return the number of times that the string "hi" appears anywhere in the given string.
count_hi('abc hi ho') -> 1
count_hi('ABChi hi') -> 2
count_hi('hihi') -> 2

Q2: Return the number of times that the string "hi" or "hello" appears anywhere in the given string.
'''