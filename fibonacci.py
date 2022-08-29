def fib():
    a =0
    b=1
    for i in range(n):
        yield a
        a , b = b, a+b

n= int(input("Enter the length of fibonacci series: "))
print("Invalid") if(n<0) else print(list(fib()))