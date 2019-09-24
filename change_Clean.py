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

def calcChange():
    #cost = getCost()
    #paid = getPay()
    C_COUNT = {0} # $100(0) $50(1) $20(2) $10(3) $5(4) $1(5) $0.25(6) $0.10(7) $0.05(8) $0.01(9)
    for i in C_COUNT:
        print(i)

def main():
    calcChange()

if __name__ == '__main__':
    main()
