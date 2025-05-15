from Multiplication_Table import create_multiplication_table, display_multiplication_table

def main():
    while True:
        # 1 & 2: Create the multiplication table and store the result
        table = create_multiplication_table()

        # 3: Display the multiplication table
        display_multiplication_table(table)

        # 4: Ask the user if they want to continue
        choice = input("\nDo you want to generate the table again? (yes/no): ").strip().lower()
        if choice not in ('yes', 'y'):
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()