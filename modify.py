'''
def modify(arr):
    arr[0]=10


arr=[1,2,3,4,5]
modify(arr)
print(arr)
'''
arr=[4,9,3,1,7,8,6,2,10]
def quickSort(arr,L,R):
    if L>=R:
        return
    left=0
    right=len(arr)-1
    P=arr[(left+right)//2]
    pivot_idx=(left+right)//2
    L=left
    R=right
    while L<R:
        # find the first left index that needs to be swapped
        while arr[L]<P:
            L=L+1
        # find the first right index that needs to be swapped
        while arr[R]>P:
            R=R-1
        arr[L],arr[R]=arr[R],arr[L]
    pivot_idx=(L+R)//2
    print(pivot_idx)
    # Sort left side
    quickSort(arr,left,pivot_idx-1)

arr=[4,9,3,1,7,8,6,2,10]
quickSort(arr,0,len(arr)-1)
print(arr)