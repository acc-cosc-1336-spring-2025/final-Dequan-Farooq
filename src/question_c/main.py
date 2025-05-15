from ancestor_consensus import get_most_likely_ancestor_consensus

def main():
    while True:
        # Prompt the user for a DNA string (greater than 8 and less than or equal to 16)
        dna_string1 = input("Enter a DNA string (greater than 8 and less than or equal to 16 characters): ").strip()
        
        # Validate the length of dna_string1
        if len(dna_string1) < 9 or len(dna_string1) > 16:
            print("Invalid DNA string length. The string must be between 9 and 16 characters.")
            continue
        
        # Prompt the user for a 4-character DNA substring
        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip()
        
        # Validate the length of dna_string2
        if len(dna_string2) != 4:
            print("Invalid DNA substring length. The substring must be exactly 4 characters.")
            continue
        
        # Call the function to get the positions of the substring
        positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        # Display the result
        if positions:
            print(f"Positions: {' '.join(map(str, positions))}")
        else:
            print("No occurrences found.")
        
        # Ask the user if they want to continue or exit
        continue_choice = input("Do you want to continue? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()