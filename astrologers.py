d=int(input("Enter the n"))
e=bool(d)
# if b==True:
#     for i in range(4,0,-1):
#         print()
#         for j in range(i):
#             print('*',end='')
if e==True:
    i=4
    for c in range(4):
        for a in range(i):
            print('*',end='')
        for b in range(1):
            print()
        i-=1
else:
    i=1
    for c in range(4):
        for a in range(i):
            print('*',end='')
        for b in range(1):
            print()
        i+=1
