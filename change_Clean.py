import sys
from os import system, name

def getCost():
    while True:
        cost = float(input("Enter the cost of the item: "))
        if cost <= 0:
            print("Value must be greater than zero.")
            continue
        else:
            break
    return cost

def getPay():
    while True:
        paid = float(input("Enter how much money was given: "))
        if paid <= 0:
            print("Value must be greater than zero.")
            continue
        else:
            break
    return paid

def calcMoney():
    cost = getCost()
    pay = getPay()

    if cost > pay:
        diff = cost - pay
        print(f"Not enough given. {round(diff,2)} is needed to cover the rest of the cost.")
    
    elif cost == pay:
        print("Cost and amount given are even. No change back needed.")

    elif cost < pay:
        remain = pay - cost
        print(f"======Change needed is ${remain}======")
        calcChange(remain)
def calcChange(remain):
    C_VALUES = [100,50,20,10,5,1,0.25,0.10,0.05,0.01]
    C_WORDVALUE = ['$100 Dollar Bills','$50 Dollar Bills','$20 Dollar Bills',
    '$10 Dollar Bills','$5 Dollar Bills','$1 Dollar Bills','Quarters','Dimes',
    'Nickels','Pennies']
    
    for v, w in zip(C_VALUES,C_WORDVALUE):
        C_COUNT = 0
        while True:
            if v <= remain:
                remain -= v
                C_COUNT += 1
                continue
            else:
                if C_COUNT > 0:
                    print(f"{C_COUNT} {w}")
                break  

def exitRun():
    while True:
        option = input("Are you sure you want to exit the program? (y/n): ")
        if option.lower() == 'y':
            print("Exiting...")
            clear()
            sys.exit()

        elif option.lower() == 'n':
            break
        
        else:
            print("Invalid option.")
            continue

def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')

def main():
    calcMoney()

    while True:
        choice = input("Would you like to enter new values? (y/n): ")
        if choice.lower() == 'y':
            clear()
            calcMoney()
        elif choice.lower() == 'n':
            exitRun()
        else:
            print("Invalid option.")
            continue

if __name__ == '__main__':
    main()