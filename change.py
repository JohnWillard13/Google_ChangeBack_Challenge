def getCost():
    cost = float(input("Enter the cost of the item to be purchased (format $X.XX): "))
    return cost

def getPay():
    pay = float(input("Enter how much money was given: "))
    return pay

def calcMoney():
    c = getCost()
    p = getPay()

    if p < c:
        needed = c - p
        print(f"Not enough cash to cover the cost. {needed} is still owed.")
    
    elif p == c:
        print("Cost fully covered, so no change is needed.")
    
    elif p > c:
        diff = p - c
        getChange(diff)

def getChange(diff):
    qCount = 0
    dCount = 0
    nCount = 0
    pCount = 0
 
#Quarter count
    while True:
        if diff >= 0.25:
            qCount += 1
            diff -= 0.25
            continue
        else:
            break

#Dime count
    while True:
            if diff >= 0.10:
                dCount += 1
                diff -= 0.10
                continue
            else:
                break

#Nickel Count
    while True:
        if diff >= 0.05:
            nCount += 1
            diff -= 0.05
            continue
        else:
            break

#Penny count
    while True:
        if diff >= 0.01:
            pCount += 1
            diff -= 0.01
            continue
        else:
            break

    print(f"Change needed is: {qCount} quarters, {dCount} dimes, {nCount} nickels, {pCount} pennies.")

def main():
    calcMoney()
    while True:
        choice = str(input("Would you like to do this again?"))
        if choice == 'y':
            calcMoney()
            continue
        
        elif choice == 'n':
            print("Exiting...")
            exit()
        
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()



