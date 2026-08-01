
def expense_tracker():
    total_amount = 0.0
    
    print("--- Welcome to Expense Tracker ---")
    print("Type 'quit' or 'exit' whenever you want to finish.\n")

    while True:
        user_input = input("Enter expense amount: ").strip()

       
        if user_input.lower() in ['quit', 'exit']:
            break

        try:
            expense = float(user_input)
            
            if expense < 0:
                print("Expense can't be negative, try again.\n")
                continue

            # Accumulator pattern
            total_amount += expense
            print(f"Added! Current Total: ${total_amount:.2f}\n")

        except ValueError:
            print("Invalid input! Please enter a valid number (e.g. 50 or 12.5).\n")

    print("\n" + "=" * 30)
    print(f"Total Expenses Saved: ${total_amount:.2f}")
    print("=" * 30)
    print("Thank you for using Expense Tracker!")

if __name__ == "__main__":
    expense_tracker()