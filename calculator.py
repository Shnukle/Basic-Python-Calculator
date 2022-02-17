print("calculator")
operator = input("what is your operator? (*, /, +, - ^) ")
first_int = input("what is your first number? ")
second_int = input("what is your second number? ")
if operator == '*':
    total = float(first_int) * float(second_int)
    print("your total is", total)

if operator == '/':
    total = float(first_int) / float(second_int)
    print("your total is", total)

if operator == '-':
        total = float(first_int) - float(second_int)
        print("your total is", total)

if operator == '+':
        total = float(first_int) + float(second_int)
        print("your total is", total)

if operator == '^':
        total = float(first_int) ** float(second_int)
        print("your total is", total)

else:
    print("invalid operator or number")