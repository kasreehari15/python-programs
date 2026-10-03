#To get the even numbers of the specified range
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
for i in range(n1,n2+1):
    if i%2==0:
        print(i)
    else:
        continue

