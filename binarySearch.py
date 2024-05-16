

#def search(arr,value):


# Objective: To find the value in a array.
# To find the midvalue (start+end)//2
# If midvalue == value, value found.
# If the mid value greater than value, need to check values in left side.
# If the mid value Less than value, need to check values in right side.
# While condition to check the whole array.

def search(arr,value):
    start=0
    end=len(arr)-1
    
    while start<end:
        midvalue=(start+end)//2

        if arr[midvalue]==value:
            return midvalue
        elif arr[midvalue]<value:
            start=midvalue+1
        else:
            end=midvalue-1
    else:
        return -1
arr=[1,3,15,250,500,1501,5000,6025]
value=1
print(search(arr,value))