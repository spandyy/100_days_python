from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {  #dict created
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  l1=[]
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)   #fetching symbols 
    l1.append(symbol)
  
  print(l1)
  syl(num1)
  def syl(num1):
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in l1:
            should_continue=False
        syl()
        # def valid_Operation(operation_symbol):
            
        #     if operation_symbol not in l1:
        #         return valid_Operation(operation_symbol)
        # valid_Operation(operation_symbol=operation_symbol)
        
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol] #getting the function 
        answer = calculation_function(num1, num2)  #calling the function by name
        print(f"{num1} {operation_symbol} {num2} = {answer}") 

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer  #if to continue with the same no then return num1=answer 
        else: 
            should_continue = False 
        calculator()

calculator()