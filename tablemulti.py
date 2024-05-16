table=int(input("Which table do you want: "))
rows=int(input("How many rows do you want to print: "))
def print_table(num,rows):
    i=1
    while i<=rows:
        print(i,'X',num,'=',i*num)
        i=i+1
print_table(table,rows)