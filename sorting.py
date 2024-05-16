'''
1. Open the file in read mode.(type of data -string)
2. Use readlines to read everyline one by one and convert them to list.
3. Store the list in new variable(arr).
4. Remove the spaces in arr using strip().
5. Convert str to int
6. arr contains unsorted elements as type int.
7. Sort the arr.
    Find the minimum value from whole array [start= 0 to end= len(arr)-1]
        compare 1st element with 2nd (take i and j as index)
        if the 1st smaller than 2nd, Take the 1st number as minimum(i) and compare with 3rd.
        else, assign j to i
        increment j to check i with next element
    Found minimum number
        Swap the minimum number to first index of arr
    Continue until all the numbers in arr changed to ascending.       
8. Open a file and store output to the file.
    Open the file in write mode - it creates a new txt file
    store the elements one by one from sorted arr.
'''








# Open a file with file name and path
file=open("numbers.txt",'r')
# To read the file use readlines(), as everyline has new content.
# create a variable and store the file to access
arr=file.readlines()
print("data present in the file\n",arr)
# The data contains list of content given file
# convert string to integer.
    # To access every 
for i in range(0,len(arr)):
    print("Actual data before strip\n",type(arr[i]),arr[i])
    arr[i]=arr[i].strip()
    arr[i]=int(arr[i])
    print("Converted to int\n",type(arr[i]),arr[i])

print('arr:\n',arr)


start=0
end=len(arr)-1
while start!=end:
    i=start                   # minimum index
    j=start+1                 # running index
    while j<len(arr):
        if arr[i] < arr[j]:
            i=i             # if i is the smallest number 
        else:
            i=j             # if j is the smallest number, assign j to i
        j=j+1
    arr[start],arr[i]=arr[i],arr[start]   # Swap minimum and start
    start=start+1           # freeze minimum

print("Sorted array:\n",arr)
F=open("sorting.txt","w")
for value in arr:
    F.write(str(value)+'\n')
F.close()