import decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000 # Set the precision to handle larger numbers
        decimal_num = decimal.Decimal(decimal_num)
        binary = ""
        while decimal_num > 0:
            binary = str(decimal_num % 2) + binary
            decimal_num = decimal_num // 2
        return binary

# Function to convert binary to decimal
def binary_to_decimal(binary_num):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000 # Set the precision to handle larger numbers
        binary_num = str(binary_num)
        decimal_num = decimal.Decimal(0)
        for i in range(len(binary_num)):
            decimal_num += int(binary_num[i]) * 2**(len(binary_num)-i-1)
        return decimal_num

# Function to perform addition of binary numbers
def binary_addition(a, b):
    decimal_a = binary_to_decimal(a)
    decimal_b = binary_to_decimal(b)
    decimal_sum = decimal_a + decimal_b
    binary_sum = decimal_to_binary(decimal_sum)
    return binary_sum

# Function to perform subtraction of binary numbers
def binary_subtraction(a, b):
    decimal_a = binary_to_decimal(a)
    decimal_b = binary_to_decimal(b)
    decimal_diff = decimal_a - decimal_b
    binary_diff = decimal_to_binary(decimal_diff)
    return binary_diff

# Function to perform multiplication of binary numbers
def binary_multiplication(a, b):
    decimal_a = binary_to_decimal(a)
    decimal_b = binary_to_decimal(b)
    decimal_product = decimal_a * decimal_b
    binary_product = decimal_to_binary(decimal_product)
    return binary_product

# Function to perform division of binary numbers
def binary_division(a, b):
    decimal_a = binary_to_decimal(a)
    decimal_b = binary_to_decimal(b)
    decimal_quotient = decimal_a / decimal_b
    binary_quotient = decimal_to_binary(decimal_quotient)
    return binary_quotient

# Function to compute absolute error
def absolute_error(actual_value, approx_value):
    return abs(actual_value - approx_value)

# Function to compute relative error
def relative_error(actual_value, approx_value):
    return absolute_error(actual_value, approx_value) / abs(actual_value)

# Scientific calculator function
def scientific_calculator():
    while True:
        print("1. Convert decimal to binary")
        print("2. Convert binary to decimal")
        print("3. Add binary numbers")
        print("4. Subtract binary numbers")
        print("5. Multiply binary numbers")
        print("6. Divide binary numbers")
        print("7. Compute absolute error")
        print("8. Compute relative error")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            decimal_num = input("Enter a decimal number: ")
            binary_num = decimal_to_binary(decimal_num)
            print("Binary equivalent:", binary_num)

        elif choice == '2':
            binary_num = input("Enter a binary number: ")
            decimal_num = binary_to_decimal(binary_num)
            print("Decimal equivalent:", decimal_num)

        elif choice == '3':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            binary_sum = binary_addition(a, b)
            print("Sum:", binary_sum)

        elif choice == '4':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            binary_diff = binary_subtraction(a,b)
            print("SUB:", binary_diff)