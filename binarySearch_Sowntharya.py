
# Objective: To find the given value present in the array or not.(in binary search method)

# Find the index of middle value in the given array to find where we need to search.
    # To find a middle value,
    # Assign start (0) and end index (len(arr)-1)
    # mid_index = (start + end) // 2
# If middle value == value, value found.
    # return the index of middle value

# If middle value < value, the value is present in the right side of middle value.
    # Freeze the numbers present before middle value.
    # Searching after middle value is enough.
    # update start = mid_index+1

# If middle value > value,  the value is present in left side of middle value.
    # Freeze the numbers present after middle value. 
    # Searching before middle value is enough.
    # update the end value to mid_index-1

# So, everytime start and end value will change based on this upto the value found.
# Repeat this until start<=end
# return -1, if the value is not present in the array.

def binarySearch(arr,value):
    start=0                     # running index to initialize start
    end=len(arr)-1              # running index to end
    while start<=end:
        mid_index=(start+end)//2
        if arr[mid_index]==value:   # value found and return the mid_index
            return mid_index
        
        elif arr[mid_index] < value: # check right side
            start = mid_index+1    # update start to number after mid_index

        else:                        # check left side
            end = mid_index-1      # decrement end to index before mid_index
    else:
        return -1
arr = [2,5,9,13,18,21,25,29,35,39,41]
value =39
print(binarySearch(arr,value))
