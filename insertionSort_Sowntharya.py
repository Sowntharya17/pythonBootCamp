'''
arr = [5,1,9,3,6,2,10]
1,5,9,3,6,2,10
1,2,5,9,3,6,10
1,2,3,5,9,6,10
1,2,3,5,9,6,10
1,2,3,5,6,9,10
1,2,3,5,6,9,10
'''
# Objective: To sort the array in ascending.
# Find the minimum value and move the minimum to 1st position.
# To mention the 1st position, create start = 0
# To find minimum,
    # Compare 1st with nearest number.
    # Set two index (i=start, j=start+1) and consider i as minimum & j as nearest number
    # If minimum > nearest number, change minimum = nearest number
    # Else, minimum = minimum, minimum not changed.
    # Compare every number with minimum and find minimum.
# Minimum stored in minimum, index--> i
# Rightshift all values and move minimum to 1st position (start).

# Rightshift all values,
    # arr[min_index] = arr[min_index-1]     min_index = value before min_index, so -1
    # arr[min_index-1] = arr[min_index-2]
    #....
    # arr[start+1] = arr[start]
    # Replace all values present before minimum except start value.
    # So, repeat this until i > start

# Move minimum to 1st position (start) and freeze.
    # increment start to freeze.
    # Repeat this upto len(arr)-1

arr = [5,1,9,3,6,2,10]  
def insertionSort(arr):
    start=0                 # store and freeze minimum
    while start<len(arr):
        i=start             # minimum stored in i
        j=start+1           # running index to check next number
        while j<len(arr):
            if arr[i] > arr[j]:
                i=j
            # otherwise i not changed, increment to check next.
            j=j+1
        minimum=arr[i]      # stored minimum   
        
        # Rightshift except start
        while i>start:
            arr[i]=arr[i-1]
            i=i-1
    # Assign minimum to 1st position (start)
        arr[start]=minimum
        start=start+1       # increment to freeze
    return arr              # return the sorted array
print(insertionSort(arr))
