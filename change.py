import sys

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
    hCount = 0
    fCount = 0
    tCount = 0
    teCount = 0
    fiCount = 0
    oCount = 0

#Hundred Dollar Count
    while True:
        if diff >= 100.00:
            hCount += 1
            diff -= 100.00
        else:
            break

#Fifty Dollar Count
    while True:
        if diff >= 50.00:
            fCount += 1
            diff -= 50.00
        else:
            break

#Twenty Dollar Count
    while True:
        if diff >= 20.00:
            tCount += 1
            diff -= 20.00
        else:
            break

#Ten Dollar Count
    while True:
        if diff >= 10.00:
            teCount += 1
            diff -= 10.00
        else:
            break

#Five Dollar Count
    while True:
        if diff >= 5.00:
            fiCount += 1
            diff -= 5.00
        else:
            break

#One Dollar Count
    while True:
        if diff >= 1.00:
            oCount += 1
            diff -= 1.00
        else:
            break

 
#Quarter count
    while True:
        if diff >= 0.25:
            qCount += 1
            diff -= 0.25
        else:
            break

#Dime count
    while True:
            if diff >= 0.10:
                dCount += 1
                diff -= 0.10
            else:
                break

#Nickel Count
    while True:
        if diff >= 0.05:
            nCount += 1
            diff -= 0.05
        else:
            break

#Penny count
    while True:
        if diff >= 0.01:
            pCount += 1
            diff -= 0.01
        else:
            break


    print(f"Change needed is: {hCount} $100 Dollar Bills, {fCount} $50 Dollar Bills, {tCount} $20 Dollar Bills, {teCount} $10 Dollar Bills, {fiCount} $5 Dollar Bills, {qCount} quarters, {dCount} dimes, {nCount} nickels, {pCount} pennies.")

def main():
    calcMoney()
    while True:
        choice = str(input("Would you like to do this again: "))
        if choice == 'y':
            calcMoney()
            continue
        
        elif choice == 'n':
            print("Exiting...")
            sys.exit()
            
        
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()



