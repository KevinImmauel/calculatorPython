from colorama import init
init()
from colorama import Fore , Style

def calculator():
    print()
    print(Fore.YELLOW,'CHOOSE AN OPTION')
    print(Style.RESET_ALL,'')
    print('A) Type an Operation')
    print('B) Only 2 operand operation') 
    print('C) Exit')
    print()
    a = input('Enter A ,B or C: ')
    if a == 'a' or a == 'A':
        op = input('Enter an Operation: ')
        ans = eval(op)
        print(Fore.GREEN,f'{op} = {ans}')
        calculator()
    elif a == 'b' or a == 'B':
        int1 = input('Enter a Number: ')
        op = input('Enter a valid operation: ')
        int2 = input('Enter another Number: ')
        ans = eval(int1 + op + int2)
        print(Fore.GREEN,f'{int1} {op} {int2} = {ans}')
        calculator()
    elif a == 'c' or a == 'C':
        exit()
    else:
        print(Fore.RED,'')
        print('ENTER A VALID OPTION')
        print(Style.RESET_ALL,'')
        calculator()

calculator()