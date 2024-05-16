#Objective: To change the given numbers to ascending order.
#To find the lowest number
    #Compare 1st number with 2nd number (required 2 index)
    #if the 1st smaller than 2nd, Take the 1st numeber and compare with 3rd.
    #if the 1st greater than 2nd, Take the 2nd amd compare with 3rd and so on.
    #Check upto the last value to find the minimum value. j<len(arr)
    # i holds minimum value
    #If i is less tan j, i didn't change. If it's greater j is the minimum. So, i=j
arr=[7,10,5,8,2,28]
new_arr=[]
while arr!=[]:
    i=0                     # minimum index
    j=1                     # running index
    while j<len(arr):
        if arr[i] < arr[j]:
            i=i             # if i is the smallest number 
        else:
            i=j             # if j is the smallest number, assign j to i
        j=j+1
    # Name minimum to the smallest value
    minimum=(arr[i])
    new_arr.append(minimum)
    arr.remove(minimum)
print(new_arr)

'''arr=[7,10,5,8,2,28]
new_arr=[]
# Continue the loop until arr gets empty.
while arr!=[]:
    i=0
    minimum=arr[0]
    while i < (len(arr)-1):
        if minimum>arr[i]:
            minimum=arr[i]
        i=i+1
    # Now the Minimum value is 2.
    # Need to remove minimum value in array elements (.remove(arr[i])
    # Add the minimum value to the new variable.
    new_arr.append(minimum)
    arr.remove(minimum)
#We have updated arr and new_arr
print(new_arr)'''



