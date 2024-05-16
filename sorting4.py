arr1=[3,7,11,16]
arr2=[22,25,15,9]
arr3=[]

# Objective: Combine the two array elements in another single array in descending order.
# Compare two maximum values in both arr1 and arr2.
# arr1 is sorted list, so maximum is last digit. while arr2 is descending, so maximum is first digit.
# So, Compare last number in arr1 and 1st number in arr2.
    # If arr1 > arr2, add arr1 to arr3 and freeze
    # Else, add arr2 to arr3 and freeze
# Compare until the length of array.

i=len(arr1)-1
j=0
while i>=0 and j<len(arr2):
    if arr1[i] > arr2[j]:
        arr3.append(arr1[i])
        i=i-1
    else:
        arr3.append(arr2[j])
        j=j+1

while i>=0 or j<len(arr2):
    if i>=0:
        arr3.append(arr1[i]) 
        i=i-1
    else:
        arr3.append(arr2[j])
        j=j+1
print(arr3)
