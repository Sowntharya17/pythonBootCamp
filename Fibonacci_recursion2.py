# Objective: To find the fibonacci of given number by recursion method.
# Store the first two fibonacci numbers in a and b
    # a=0, b=1
# To find fibonacci(8),
    #  define a function  with variable n.
    #   use global variable to access the variable outside function definition.
    #   function will check fibonacci(8) in fibonacci(n-1) and return.
    #   check and return until n<2. Because, 0 and 1 are first 2 fibonacci numbers.
#   If n is 1, we don't need to find fibonacci as it was known. So, return.
# return to the previous step (i.e, n=2)
    # fibonacci is addition of previous two fibonacci numbers.
    # num = a+b, fibonacci stored in num.
    # update a to b and b to num to find next fibonacci number.

a=0
b=1
print(a)
print(b)
def fibonacci(n):   # function definition
    global a
    global b
    if  n<2:
        return
    fibonacci(n-1)  # function call
    num=a+b
    a=b
    b=num
    print("index of fibonaci number",n)
    print(num)
    return
fibonacci(8)        # function call