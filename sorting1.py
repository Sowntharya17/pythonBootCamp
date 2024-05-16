'''
arr = 25,7,15,12,5,20 
7,25,15,12,5,20 - 0,1
7,15,25,12,5,20 - 1,2
7,15,12,25,5,20 - 2,3
7,15,12,5,25,20 - 3,4
7,15,12,5,20,25 - 4,5; freeze 25
7,15,12,5,20,25 - 0,1
7,12,15,5,20,25 - 1,2
7,12,5,15,20,25 - 2,3
7,12,5,15,20,25 - 3,4
7,12,5,15,20,25 - 4,5; freeze 20,25
7,5,12,15,20,25 - 0,1
7,5,12,15,20,25 - 1,2
7,5,12,15,20,25 - 2,3
7,5,12,15,20,25 - 3,4
5,7,12,15,20,25 - 4,5; freeze 15,20,25
5,7,12,15,20,25 - 0,1
5,7,12,15,20,25 - 1,2
5,7,12,15,20,25 - 2,3
5,7,12,15,20,25 - 3,4
5,7,12,15,20,25 - 4,5; freeze 12,15,20,25
5,7,12,15,20,25 - 0,1
5,7,12,15,20,25 - 1,2
5,7,12,15,20,25 - 2,3
5,7,12,15,20,25 - 3,4
5,7,12,15,20,25 - 4,5; freeze 7,12,15,20,25
arr = 25,7,15,12,5,20
'''
# Objective: To sort the given array in ascending.
# Compare the 1st number(i) with 2nd number(j),
    # if 1st number is greater than 2nd, swap least number to left.(i,j=j,i)
    # if not, no need to swap.
    # Next compare (2nd & 3rd), (3rd & 4th) and so on.(increment i and j)
    # Compare every number with the nearest number upto the last number(len(arr)-1).
    # Everytime we moved the minimum to left and maximum to right.
    # So the largest number in the array moved to last.
# Freeze maximum.
# Create a variable to assign ending point of the loop to Freeze maximum.
# end=len(arr)-1
# Decrement end to freeze the end everytime
# Repeat this until the end value contains more than one element.

arr=[25,7,15,12,5,20]
#print(arr)
#start=0
end=len(arr)-1
while end>1:
    i=0
    j=1
    while j <len(arr):
        if arr[i] > arr[j]:
            #print('i=',arr[i],'j=',arr[j])
            arr[i],arr[j] = arr[j],arr[i]
            #print(arr)
        else:
            arr[i],arr[j] = arr[i],arr[j]
            #print(arr)
        i=i+1
        j=j+1
        print(arr)
    print(arr)
    end=end-1
print(arr)