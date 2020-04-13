import sys

if len(sys.argv[1:]) == 1:
    if sys.argv[1].isnumeric() == 0:
        print("ERROR")
    elif int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    elif int(sys.argv[1]) % 2 == 1:
        print("I'm Odd.")
if len(sys.argv[1:]) > 1:
    print("ERROR")
