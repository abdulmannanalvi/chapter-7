n = int(input("Enter the No:"))

for i in range(2,n):
    if (n%i)==0:
        print("Not a Prime No")
        break
    else:
        print("No is prime")
        break