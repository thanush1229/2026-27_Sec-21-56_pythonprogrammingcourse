num = int(input("Enter a number: "))
original_number = num
digit_count = 0

if num == 0:
    digit_count = 1
else:
    while digit_count <= num: 
    
        digit_count = digit_count + 1 # increase the count by 1
        number = number // 10  # remove the last digit with // 10

print(f"Number of digits in {original_number} is {digit_count}")