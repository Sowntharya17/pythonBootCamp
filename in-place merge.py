# Merge inplace of given array.
# Define a function mergeInplace and mention the arguments arr,first,second,end.
# Compare the values of first and second,
    # if first > second:
        # minimum=second, Temporary variable
        # store minimum index to min_index and use for rightshift. So that the value of second will not change after rightshift.
        # min_index = second
        # rightshift all values before minimum
            # arr[min_index] = arr[min_index-1]
            # arr[min_index-1] = arr[min_index-2]
            # ....
            # arr[first+1] = arr[first]
            # continue this loop until first>second
        # assign first = minimum
        # increment both first and second as
    # else:
        # minimum = first
        # increment first
# Continue this until first and second reached to end
'''
arr=[2,4,6,1,3,5]
first=0
mid_index = len(arr)//2
second = mid_index
while first<len(arr) and second<len(arr):
    if arr[first] > arr[second]:
        minimum=arr[second]
        min_index=second
        while min_index>first:
            arr[min_index]=arr[min_index-1]
            min_index=min_index-1
        print(arr)
        arr[first]=minimum
        first=first+1
        second = second+1
    else:
        first=first+1
print(arr)
'''
def mergeInplace(arr, first, second, end):
    # code here
    while second<=end and first<second:
        if arr[first] > arr[second]:
            minimum=arr[second]     # store minimum in temporary variable(minimum)
            min_index=second        # store min_index to new variable.second will not change.
            while min_index>first:  # rightshift upto min_index > first
                arr[min_index]=arr[min_index-1]
                min_index=min_index-1       # decrement to rightshift next element
            arr[first]=minimum      # assign minimum to first
            print(arr)
            first=first+1
            second = second+1
        else:
            first=first+1       
    return arr
arr=[2,4,6,1,3,5]
print (mergeInplace(arr, 0, 3, len(arr) - 1))       # funtion call
