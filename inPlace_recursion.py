'''
2,4,6,1,3,5
F     S       2>1=F>S
1,2,4,6,3,5 
  F     S     2<3=F<S
1,2,4,6,3,5
    F   S     4>3=F>S
1,2,3,4,6,5
      F   S   4<5=F<S
1,2,3,4,6,5
        F S   6>5=F>5
'''
def mergeInplace_recursion(arr, first, second, end):
    if first>=second or second>end:
        return arr
    
    if arr[first]>arr[second]:
        min_value=arr[second] # store minimum in temporary variable
        s=second              # store min_value to new variable.second will not change.
        while s>first:
            arr[s]=arr[s-1]
            s=s-1
        arr[first]=min_value    # assign min_value to first  
        
        mergeInplace_recursion(arr, first+1, second+1, end) #function call
    else:
        mergeInplace_recursion(arr, first+1, second, end)
    
    return arr
arr = [2,4,6,1,3,5]
mergeInplace_recursion(arr, 0, 3, len(arr)-1) #main function call
print(arr)