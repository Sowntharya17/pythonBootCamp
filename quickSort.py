'''
4,9,3,1,7,8,6,2,10
L               R   L<P, R>P    +L
4,9,3,1,7,8,6,2,10  
  L             R   R>P, R>P    -R
4,9,3,1,7,8,6,2,10
  L           R     L>P, R<P    Swap
4,2,3,1,7,8,6,9,10
  L           R     L<P, R>P    +L
4,2,3,1,7,8,6,9,10
    L         R     L<P, R>P    +L
4,2,3,1,7,8,6,9,10
      L       R     L<P, R>P    +L

'''
def quickSort(arr,L,R,level):
    # Find the pivot value and rearrange small element to left and large to right.
    # Sort the left array in ascending.
    # Sort the right side array in ascending.
    print('level',level)
    print('arr',arr[L:R+1])
    # Rearrange values before pivot as smaller and values after pivot as larger elements.
    # Assign arr[(L+R)//2] as pivot.
    if L>=R:
        return
    # pivot value for rearrangement
    P=arr[(L+R)//2]
    i=L       # running index i and j
    j=R
    while i<j:
        # find the first left index that needs to be swapped
        while arr[i]<P:
            i=i+1
        # find the first right index that needs to be swapped
        while arr[j]>P:
            j=j-1
        arr[i],arr[j]=arr[j],arr[i]
        #array after rearranging, arr=[4,2,3,1,6,7,8,9,10]
        #[1,2,3,4,6]
    print('New', arr[L:R+1])
    # Store the pivot index to handle function call for left and right
    pivot_idx=i

    # Sort left side
    quickSort(arr,L,pivot_idx-1,level+1)
    print('back to level', level)
    # Sort right side
    quickSort(arr,pivot_idx+1,R,level+1)
    print('completed level', level)
    
#arr=[4,9,3,1,7,8,6,2,10]
arr=[4,9,3,1,7,8,6,2,10]
quickSort(arr,0,len(arr)-1,0)
print(arr)