import sys
if len(sys.argv[1:]) == 2:
    if (sys.argv[1].isnumeric() == 0) | (sys.argv[2].isnumeric() == 0):
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
    else:
        print("Sum:\t\t" + str(int(sys.argv[1]) + int(sys.argv[2])))
        print("Difference:\t" + str(int(sys.argv[1]) - int(sys.argv[2])))
        print("Product:\t" + str(int(sys.argv[1]) * int(sys.argv[2])))
        if int(sys.argv[2]) != 0:
            print("Quotient:\t" + str(int(sys.argv[1]) / int(sys.argv[2])))
            print("Remainder:\t" + str(int(sys.argv[1]) % int(sys.argv[2])))
        else:
            print("Quotient:\tERROR (div by zero)")
            print("Remainder:\tERROR (modulo by zero)")
elif len(sys.argv[1:]) == 0:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")
elif len(sys.argv[1:]) > 1:
    print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")

