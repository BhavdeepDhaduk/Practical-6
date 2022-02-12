"""BHAVDEEP DHADUK -20CE024
Practical 6: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification."""

n = int(input())  # take int input
arr = []
for i in range(n):  # loop for append elements in arr
    s = input()
    arr.append(s)
set1 = set(arr)  # convert arr into set to reduce duplication
print(len(set1))  # print total distinct number of elements
arr2 = []
arr3 = []
for i in arr:  # loop for count the total number of duplication of each word
    if i in arr2:  # if elements at ith index  present in arr2 then pass
        pass
    else:
        arr2.append(i)  # else append that element into arr2
        # count the duplication of perticular element and append in arr3
        arr3.append(arr.count(i))
for i in arr3:
    print(i, end=' ')  # print the count