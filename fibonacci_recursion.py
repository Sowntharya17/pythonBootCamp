# 0,1                           index0,1
# 0+1=1 --> 0,1,1               index2
# 1+1=2 --> 0,1,1,2             index3
# 1+2=3 --> 0,1,1,2,3           index4
# 2+3=5 --> 0,1,1,2,3,5
# 3+5=8 --> 0,1,1,2,3,5,8
# 5+8=13--> 0,1,1,2,3,5,8,13
# 8+13=21-->0,1,1,2,3,5,8,13,21 index8

# print fibonacci(10)

# To find Fibonacci series of given index
    # Store first 2 fibonacci numbers 0 and 1
        # Assign a=0 and b=1 and print
    # Fibonacci number---> Addition of two previous number
        # fibonacci=a+b
    # Update a and  b to find next fibonacci numeber, a=b, b=fibonacci

i=8      # Given index
a=0         # fibonacci number1
b=1         # fibonacci number2
print(a)
print(b)
j=2         # Running index
while j<=i:
    print("index",j)
    fibonacci=a+b
    a=b
    b=fibonacci
    j=j+1
    #print(fibonacci)
print('fibonacci of ',i,'is',fibonacci)

'''
for num in range(i-1):
    fibonacci=a+b
    a=b
    b=fibonacci
print(fibonacci)
'''
