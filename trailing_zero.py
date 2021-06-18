#Calculate the factorial of a given number
#Find the number of trailing zeros in that factorial.
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
a=int(input("Enter the no. for factorial\n"))
b=fact(a)
print("factorial is",b)
# def t_zero(b):
#     i=0
#     while True:
#         if b%10==0:
#             b=b/10
#             i+=1
#         else:
#             break
#     return i
# c=t_zero(b)
# print('trailing zero is',c)
def t_zero(a):
    x=0
    while(a>=5):
        a=a//5
        x=x+a
    return x
print('trailing zero',t_zero(a))