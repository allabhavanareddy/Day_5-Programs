# Input the number for which you want to print the multiplication table
num = int(input("Enter a number: "))

# Specify the range (in this example, we print the table from 1 to 10)
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
