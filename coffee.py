def main():
    amount_due = 75

    while amount_due > 0:
        print("Amount due:", amount_due, "p")
        coin = get_coin()
        amount_due = update_total(amount_due, coin)

    dispense_product(amount_due)

def get_coin():
    while True:
        coin = int(input("Insert coin: "))
        if coin in [50, 20, 10, 5]:
            return coin
        else:
            print("Enter a correct denomination of either 50p, 20p, 10p, or 5p ")


def update_total(current, coin):
    return current - coin


def dispense_product(amount_due):
    print("Change owed:", -amount_due, "p")


main()
