
# To find the given value in the array element.
# Check the array one by one (Loop can be used).
# if the value match, return true (if condition)
# if the value not match, check next.(increment)
# if nothing match return false.
# Check upto last digit (Condition - len-1)

def search(arr,value):
    '''i=0
    while i<len(arr):
        if arr[i]==value:
            return True
        else:
            i=i+1
    return False'''
    i=len(arr)-1
    while i>=0:
        if arr[i]==value:
            return True
        else:
            i=i-1
    return False

arr=[1,3,15,22,250,360,440,500,1000,1501,5000,5320,6025]
value=500
print(search(arr,value))