#import art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
  #print(art.logo)
  print("logo")
  should_continue = True
  n1 = float(input("What´s the first number:"))
  while should_continue:
    for symbol in operations:
      print(symbol)
    operator = input("Pick an operation:")
    while operator not in operations:
      print("please type a valid option")
      operator = input("Pick an operation:")
    n2 = float(input("What´s the second number:"))
    result = operations[operator](n1=n1, n2=n2)
    print(f"{n1} {operator} {n2} = {result}")
    option = input(f"Type 'y' to continue calculation with {result} or type 'n' to start a new calculation: ").lower()
    if option == 'y':
      n1 = result
    else:
      should_continue= False
      print("\n"*100)
      #Recursive function call
      calculator()
 
calculator()

