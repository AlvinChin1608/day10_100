# simple calculator 
from art import logo

# add
def add(n1, n2):
  return n1 + n2

# minus
def sub(n1, n2):
  return n1 - n2

# multi
def mul(n1, n2):
  return n1 * n2

# divide
def div(n1, n2):
  return n1 / n2

# Dictionary of operations
operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

for k in operations:
  print(k)

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True 
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    function = operations[operation_symbol]
    result = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}\n\n")
    userinput = input(f"Type'y'to continue calculating with {result}, or type 'n' to start a new calculation: \n\n")
    if userinput == "y":
      num1 = result
    else:
      should_continue == False
      calculator()
calculator()

