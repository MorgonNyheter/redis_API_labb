import get_quote
import add_quote


def menu():
    print("1. Get a random quote")
    print("2. Add a quote")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    while True:
        choice = menu()
        if choice == "1":
            quote = get_quote.get_random_quote()
            print(f"Author: {quote['author']}\nQuote: {quote['quote']}\n")
        elif choice == "2":
            quote = input("Enter the quote: ")
            author = input("Enter the author: ")
            add_quote.add_quote(quote, author)
            print("Quote added successfully.\n")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
