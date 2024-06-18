from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculate():
  print(logo)
  num_1 = float(input("What's the first number?: "))
  
  for key in operations:
    print(key)

  again = True
  while again is True:
    operation_symbol = input("Pick an operation: ")
    num_2 = float(input("What's the next number?: "))
    operation_result = operations[operation_symbol](num_1, num_2)
    
    print(f"{num_1} {operation_symbol} {num_2} = {operation_result}")
    print(f"The result is {operation_result}.")
    
    run_again = input(f"Do you want to continue with the result number {operation_result}? Type 'yes' to continue or 'no' to start a new calculation. ")
    if run_again == "no":
      again = False
      calculate()
    elif run_again == "yes":
      again = True
      num_1 = operation_result

calculate()
