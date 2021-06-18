# WAP which will keep adding a stream of number inputted by the user. The adding stops as soon
#as user presses q key on the keyboard.
print("Enter the price value")
sum=0
while True:
    a=(input())
    if a=='q':
        print("Total sum is", sum)
        break
    else:
        sum=sum+int(a)
        
    