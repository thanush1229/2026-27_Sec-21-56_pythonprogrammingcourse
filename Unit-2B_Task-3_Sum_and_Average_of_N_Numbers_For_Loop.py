n = int(input("Enter N: "))
sum = 0

for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum + num

average = sum / n

print("Sum =", sum)
print("Average =", average)