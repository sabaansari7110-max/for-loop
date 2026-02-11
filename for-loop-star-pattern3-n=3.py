#print star pattern
#  .    .
#  ..   ..
#  ...  ...  n= 3

n= int(input("enter a number"))

for i in range(1, n+1):
    print("*"*i, end= "")
    print(" "* (n-2), end= "")
    print("*"* i, end= "")

    print("\n")
