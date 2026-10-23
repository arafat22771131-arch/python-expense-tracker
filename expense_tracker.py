
import csv
from pathlib import Path
from datetime import date

FILE = Path("expenses.csv")

def add_expense():
    name = input("Expense name: ").strip()

    try:
        amount = float(input("Amount: "))

        if not name or amount <= 0:
            print("Enter a name and an amount greater than zero.")
            return

        new_file = not FILE.exists()

        with FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if new_file:
                writer.writerow(["Date", "Name", "Amount"])

            writer.writerow([date.today(), name, amount])

        print("Expense saved!")

    except ValueError:
        print("Enter a valid amount.")

def show_expenses():
    if not FILE.exists():
        print("No expenses recorded yet.")
        return

    total = 0

    with FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        print("\n--- Expense History ---")

        for row in reader:
            amount = float(row["Amount"])
            total += amount
            print(f'{row["Date"]} | {row["Name"]} | {amount:.2f}')

    print(f"Total expenses: {total:.2f}")

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
