'''
35,45,7,3,25
3,45,7,35,25
3,7,15,35,25
3,7,15,25,35
3,7,15,25,35
'''
# Objective: To change the array elements in ascending order.
# To sort, find the minimum value in the array.
    # Assign first value as minimum
    # Compare minimum with 2nd element
    # If minimum lessthan 2nd element, minimum value remains same
    # If mininum greaterthan 2nd element, update 2nd element as minimum value
    # Continue this upto len(arr)-1
# Swap the minimum value with first index of arr.
# Freeze the first element, update the start index and repeat the steps with remaining elements.
# Repeat this upto the start=len(arr)-1

arr=[35,45,7,3,25]
start=0
while start<len(arr)-1:
    # Get 2 variables to compare first 2 index values
    minimum=start           # minimum index
    a=start+1               # running index
    while a<len(arr):
        if arr[minimum] < arr[a]:
            minimum=minimum
        else:
            minimum=a
        a=a+1
    print("minimum index", minimum)
    print("minimum element",arr[minimum])
    arr[start],arr[minimum] = arr[minimum], arr[start]
    print(arr)
    start=start+1
print(arr)