import art
logo = art.logo

# part one
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

key = ["+", "-", "*", "/"]

# part two
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
# result = operations["*"](4, 8)

# Calculator program
print(logo)
# set the two while loops to True
calculator = True
new_calc = True
# calculator loop
while calculator:
    # new calculation loop
    if new_calc:
        # ask the user for 1st input
        n1 = float(input("What's the first number? "))

    # calculation function
    def calculator_loop(n1):
        print("+\n-\n*\n/")
        # input operation
        op = input("Pick an operation: ")
        # ask the user for 2nd input
        n2 = float(input("What's the next number? "))
        #check what operation was used
        if op == "+":
            # calculate and store it in var result
            result = operations["+"](n1, n2)
            # return 3 variables
            return result, op, n2
        elif op == "-":
            result = operations["-"](n1, n2)
            return result, op, n2
        elif op == "*":
            result = operations["*"](n1, n2)
            return result, op, n2
        elif op == "/":
            result = operations["/"](n1, n2)
            return result, op, n2

    # unpack the outside scope variables back into the calculator_loop
    calc_result, calc_op, calc_n2 = calculator_loop(n1)
    # grab the returned variables and print them in an f-string
    print(f"{n1} {calc_op} {calc_n2} = {calc_result}")
    # ask the user for another round with the result or a new number
    decision = (input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation: "))
    if decision == 'y':
        n1 = calc_result
        new_calc = False
    else:
        new_calc = True
