# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?
# Further Exploration - Consider adding a way for the user to specify the starting 
# and ending values of the odd numbers printed.

def odd_numbers(n1, n2):
    if n1 % 2 == 0:
        n1 += 1
    for i in range(n1, n2 + 1, 2):
        print(i)
    

number1 = int(input("Enter the starting integer: "))
number2 = int(input("Enter the ending integer: "))

odd_numbers(number1, number2)
