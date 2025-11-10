# Program: Naive String Matching Algorithm
# Objective: Find all occurrences of a pattern within a text using the naive approach

def naive_string_match(text, pattern):
    """
    This function searches for all occurrences of 'pattern' in 'text'.
    It checks every possible position in the text.
    """
    n = len(text)
    m = len(pattern)
    positions = []  # List to store all match positions

    # Slide pattern over text one by one
    for i in range(n - m + 1):
        # Compare substring of text with pattern
        if text[i:i+m] == pattern:
            positions.append(i)  # Pattern found at index i

    return positions


def main():
    text = ""
    pattern = ""

    while True:
        print("\n===== Naive String Matching Menu =====")
        print("1. Enter Text String")
        print("2. Enter Pattern String")
        print("3. Search Pattern in Text")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text string: ")

        elif choice == "2":
            pattern = input("Enter the pattern string: ")

        elif choice == "3":
            if len(pattern) > len(text):
                print("Error: Pattern length cannot be greater than text length.")
            elif text == "" or pattern == "":
                print("Please enter both text and pattern first.")
            else:
                matches = naive_string_match(text, pattern)
                if matches:
                    print(f"Pattern found at starting indices: {matches}")
                else:
                    print("No match found.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


# Run program
if __name__ == "__main__":
    main()
