# FinalTestWork1.py file,, Python code.
# Task: From the array of strings entered from the console, the new array should be
# formed containing strings whose length is not more than three characters
#
size1 = int(input("Please enter size of the string array: "))
print('Please enter all elements of this array separated by ENTER')
array1 = [0] * size1
array2 = []
size2 = 0
#
for index in range(size1):
    # To fill array1 by entering strings from the console
    array1[index] = input()
    if(len(array1[index]) <= 3):
        size2 += 1
        if(size2 > 1):
            # To fill array2
            array2.append(array1[index])
        else:
            array2[0] = array1[index]
# To write array1 and array2
print(array1,' -> ',array2)
