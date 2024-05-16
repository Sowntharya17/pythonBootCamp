'''
25,50,8,65,5,15
5,50,8,65,25,15
5,8,50,65,25,15
5,8,15,65,25,50
5,8,15,25,65,50
5,8,15,25,50,65
'''
# Objective: To change the given numbers in ascending order without using empty variable.
# Find the minimum value in a given set of numbers.
    # By comparision method
    #Compare 1st number with 2nd number
    #if the 1st smaller than 2nd, Take the 1st numeber and compare with 3rd.
# Found minimum number
    # Replace the minimum number to first index of search array.
    # Move the actual 1st number to the place where the minimum number present.
# Continue until all the numbers changed to ascending.
arr=[25,50,8,65,5,15]
start=0
end=len(arr)-1
print(arr)
while start!=end:
    print("Step/Start:",start)
    i=start                   # minimum index
    j=start+1                 # running index
    while j<len(arr):
        if arr[i] < arr[j]:
            i=i             # if i is the smallest number 
        else:
            i=j             # if j is the smallest number, assign j to i
        j=j+1
    print("index of minimum",i)
    print("Minimum",arr[i])
    #arr[i] is the minimum holder
    arr[start],arr[i]=arr[i],arr[start]   # Swap minimum and start. Create a new variable to indicate swap.
    start=start+1
    print(arr)              # increment to freeze the swaped minimum.
print(arr)