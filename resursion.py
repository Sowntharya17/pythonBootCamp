'''
printupto(5) - printupto(4),4
printupto(4) - printupto(3),3,4
printupto(3) - printupto(2),2,3,4
printupto(2) - printupto(1),1,2,3,4
printupto(1) - printupto(0),0,1,2,3,4
printupto(0) - return
'''

def printUpto(n):   # function definition
    if n==0:
        return
    printUpto(n-1)  # function call
    print(n-1)
    return
printUpto(5)        # function call

'''
printUpto(4),4
printUpto(3),3,4
printUpto(2),2,3,4
printUpto(1),1,2,3,4
printUpto(0),0,1,2,3,4   (ignore -ve)
'''
