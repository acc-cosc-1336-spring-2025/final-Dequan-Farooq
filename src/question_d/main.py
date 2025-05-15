from stock_2 import get_stock_list

def create_stock_file(stocks, filename="stock_file.dat"):
    with open(filename, 'w') as file:
        for stock in stocks:
            file.write(f"{stock.get_symbol()} {stock.get_company_name()}\n")


def display_stock_list(stocks):
    print("\nStock Purchase History:")
    for stock in stocks:
        print(f"Symbol: {stock.get_symbol()}, Company: {stock.get_company_name()}")
    print()


def main():
    stocks = get_stock_list()
    create_stock_file(stocks)

    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_stock_list(stocks)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()