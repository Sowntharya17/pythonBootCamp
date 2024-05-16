
#0,1,1,2,3,5,8,13,21,34


def fibonacci(n):
    if n==1:
        return n
    elif n==0:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
fibonacci(8)
print(fibonacci(8))
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(8)
print("fibonacci number is",fibonacci(8))
'''
