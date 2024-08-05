import sys

def add(num1, num2):
    add= num1 + num2
    return(add)

def sub(num1, num2):
    s= num1 - num2
    return(s)

num = float(sys.argv[1])
operation = sys. argv[2]
num = float(sys.argv[3]

if operation == "add":
     output = add (num1, num2)
     print(output)
