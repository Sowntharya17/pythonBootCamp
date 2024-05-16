'''
3,7,1,5,2,4
1,3,7,5,2,4
1,2,3,7,5,4
1,2,3,7,5,4
1,2,3,4,7,5
1,2,3,4,5,7
'''
#Objective: Convert the array elements in ascending order.
# Find the minimum value in the array. (from start index)
    # Set the first number as minimum (index i)
    # Compare the first number with nearest number (index j)
    # If the minimum is greater than nearest number, change the minimum as nearest number.
    # If the minimum is smaller than nearest element, minimum will not change
    # Compare the minimum with every elements in the unsorted array and find minimum.
# Minimum value stored in the variable (minimum).
# Minimum index stored in the variable (min_index).
# Right shift all the values present before minimum.
    # arr[min_index]=arr[min_index-1] --> arr[i] = arr[i-1], i=min_index
    # arr[min_index-1]=arr[min_index-2], arr[i-1]=arr[i-2]
    # ...
    # update every index value except start
    # i.e, arr[start+1]=arr[start], change upto i=start+1
    # Condition to change upto all the index present before minimum except start. (i>start)
# Assign the minimum to 1st place (start)
# freeze the 1st value (start). Increment start index.
# Repeat the steps upto the final value in the array(to len(arr)-1)

arr=[3,7,1,5,2,4]
print(arr)
start=0
while start<len(arr):   # To run the inner lopp upto len(arr)-1
    i=start             # Minimum holder
    j=start+1           # Running index
    while j<len(arr):
        if arr[i] > arr[j]:
            i=j
        else:
            i=i
        j=j+1
    minimum=arr[i]      # store minimm value to a variable minimum
    min_index=i
    while i>start:      # Rightshift upto the element before start
        arr[i]=arr[i-1]
        print('minimum index',i)
        print('rightshift element',arr[i-1])
        i=i-1
        print(arr)
    print('starting index',start)
    print('minimum value',minimum)
    # move minimum to start index
    arr[start]=minimum
    print('arr = ',arr)
    start=start+1
print('Sorted array',arr)
