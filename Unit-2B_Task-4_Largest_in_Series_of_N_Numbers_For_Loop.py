n = int(input("Enter N: "))
largest = int(input("Enter a number: "))

for i in range(n - 1):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)