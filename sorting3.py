arr1 = [1,2,5,7,9]
arr2 = [3,4,6,8,10,15,18]
arr3=[]
# Objective: Merge and convert the two sorted arrary to single sorted array.
# Compare the first number in both the array, arr1 and arr2.
    # if arr1 < arr2, add arr1 to arr3 and freeze that number in arr1
    # Else, add arr2 to arr3 and freeze that number in arr2
    # Compare the second number with the maximum of previous comparison.
    # Repeat this upto the last number in the array.
'''
1<3 --> arr3=[1]
2<3 --> arr3=[1,2]
5>3 --> arr3=[1,2,3]
5>4 --> arr3=[1,2,3,4]
5<6 --> arr3=[1,2,3,4,5]
7>6 --> arr3=[1,2,3,4,5,6]
7<8 --> arr3=[1,2,3,4,5,6,7]
9>8 --> arr3=[1,2,3,4,5,6,7,8]
9<10--> arr3=[1,2,3,4,5,6,7,8,9]
arr1=[], arr2=[10]
arr3=[1,2,3,4,5,6,7,8,9,10]
'''
# Once checking all numbers in arr1 or arr2, Check the two index value after the loop.
# Both the indeces should equal to the length of array.
# If not, we have remaining unchecked numbers in that array.
#  Add all the remaining element directly to arr3 as it is sorted list.
    # If i < len(arr1), it has unchecked numbers. Add it to arr3.
    # If j < len(arr2), it has unchecked numbers. Add it to arr3.
    # If it has more than one number, increment i and j to add all one by one.


i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i=i+1
    else:
        arr3.append(arr2[j])
        j=j+1
print(i)
print(j)

while i<len(arr1) or j<len(arr2):
    if i<len(arr1):
        arr3.append(arr1[i]) 
        i=i+1
    else:
        arr3.append(arr2[j])
        j=j+1

print(i)
print(j)
print(arr1)
print(arr2)
print(arr3)