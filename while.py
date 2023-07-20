#ask user to enter the number
#if the user enters a negative number, program should stop asking the user for input
#calculate the average of the numbers entered excluding the negative
#compile, save, run code
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    numbers.append(num)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers entered is {average}")
else:
    print("You didn't enter any numbers.")