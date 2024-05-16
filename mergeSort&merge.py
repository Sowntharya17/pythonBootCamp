
# Split the array by 2 parts until the arr>1
    # if len of arr >1, find mid value
    # assign left and right value (value upto mid=left), (mid to end - right)
# if len(arr)<=1, create empty array arr3
    # if left < right
        #add left to arr3
    # if left > right
        #add right to arr3

# arr=[15,5,40,26,30,13,8,3]
# left = 15,5,40,26
# left = 15,5, right = 40,26
# left = 15, right = 5  , left=40, right=26
# left_sort = 15, right_sort = 5, left_sort = 40, right_sort = 26, 
# return merge(arr3) = 5,15,  return merge(arr3) = 26,40


def mergeSort(arr):
    if len(arr)<=1:     # break recursion
        return arr
    mid_index=len(arr)//2
    left=arr[:(mid_index)]
    right=arr[(mid_index):]
    print(left)
    print(right)
    left_sort = mergeSort(left)
    right_sort = mergeSort(right)
    print(left_sort)
    print(right_sort)
    return merge(left_sort,right_sort)  # call merge function

# Sort the array in each step
# Create a empty array to store sorted values
# Assign two index values, i for left, j for right
def merge(left_sort,right_sort):
    arr3=[]
    print(arr3)
    i=0
    j=0
    while i<len(left_sort) and j<len(right_sort):
        if left_sort[i] < right_sort[j]:
            arr3.append(left_sort[i])
            i=i+1
        else:
            arr3.append(right_sort[j])
            j=j+1

# while i<len(left) or j<len(right) add remaining to arr3
    while i<len(left_sort):
            arr3.append(left_sort[i]) 
            i=i+1
    while j<len(right_sort):
            arr3.append(right_sort[j])
            j=j+1
    return arr3
arr=[8,15,12,5,3,25,1,10]
print(mergeSort(arr))

