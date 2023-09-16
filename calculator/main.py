def add(a,b):
    return a+b

def subtract ( a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b==0:
        print( " cant happen")
        return 0
    else:
        return a/b
    
while True:
    print("\nSelect operation:")
    print ("q. Quit")
    print("1.Add")
    print("2.subtract")
    print("3. Multiplication")
    print("4. divide")

    choice = input( "Enter choice ")

    if choice == 'Q':
        break
    if choice in [ '1', '2', '3', '4']:
        num1 = float (input(" Enter first number: "))
        num2 = float(input( " Enter second number: "))
        if choice == '1':
            result = add( num1, num2)
            print( "anser is", result)
        elif choice == '2':
            result = subtract( num1, num2)
            print( "anser is", result)
        elif choice == '3':
            result = multiply( num1, num2)
            print( "anser is", result)
        elif choice == '4':
            result = divide(num1, num2)
            print( "anser is", result)
        else:
            print("invalid")

