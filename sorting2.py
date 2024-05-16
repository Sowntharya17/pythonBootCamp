'''
arr = 25,7,15,12,5,20 
7,25,15,12,5,20 - 0,1 swap
7,15,25,12,5,20 - 1,2
7,15,12,25,5,20 - 2,3
7,15,12,5,25,20 - 3,4
7,15,12,5,20,25 - 4,5; freeze 25
7,15,12,5,20,25 - 0,1
7,12,15,5,20,25 - 1,2
7,12,5,15,20,25 - 2,3
7,12,5,15,20,25 - 3,4; freeze 20,25
7,12,5,15,20,25 - 0,1
7,5,12,15,20,25 - 1,2
7,5,12,15,20,25 - 2,3; freeze 15,20,25
5,7,12,15,20,25 - 0,1
5,7,12,15,20,25 - 1,2; freeze 12,15,20,25
5,7,12,15,20,25 - 0,1; freeze 7,12,15,20,25

'''
# Objective: To sort the given array in ascending.

# arr--> unsorted array (0 to n-1)
# Compare the 1st and 2nd number: if 1st>2nd number, swap. else, no swap.
# Compare the 2nd and 3rd number: if 3rd>4th, do swap.
# Continue this upto last two numbers.
# Highest number moved to last(n-1).

# Now, Unsorted array (0 to n-2)
# Compare the 1st and 2nd number: if 1st>2nd number, swap. else, no swap.
# Compare the 2nd and 3rd number: if 3rd>4th, do swap.
# Continue this upto last two numbers.
# Highest number moved to last(n-2).
# ......
# Continue this upto unsorted array (index 0 to index 1)
#--------------------------------------------------------------------------------

# end=len(arr)-1
# while end >=1:
# To compare all numbers with nearest number.
    # first = 0
    # while first < end:
        # if first>first+1:
            #Swap first and first+1
        # increment to check next two numbers(first=first+1)
    # decrement end by 1.


arr=[25,7,15,12,5,20]
end=len(arr)-1
while end>=1:
    i=0
    while i<end:
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        i=i+1
    end=end-1
    print(arr)
print(arr)