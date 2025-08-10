# Displaying multiplication tables using "for" loops
n = int(input("Enter the table number: "))

for i in range(1, 11):  # Loop through numbers from 1 to 10
    result = n * i
    print(f"{n} x {i} = {result}")