
from transaction import Transaction
from store import Exporter , CsvExporter , save__to_file,load_file
class FinanceTracker:
    def __init__(self):
        self.transactions = load_file()
        self.budget = {
            "food": 0,
            "salary":0,
            "entertainment": 0,
            "other": 0
        }
    def add_transaction(self, amount, category, description, t_type):
        try:
            transaction = Transaction(amount, category, description, t_type)
            self.transactions.append(transaction)
            #  # Budget check
            if t_type == "expense" and category in self.budget:
                if self.budget[category] > 0 and amount > self.budget[category]:
                    spent = sum (t.amount for t in self.transactions if t.category == category and t.t_type == "expense")
                    if spent + amount > self.budget[category]:
                        print(f"Warning: Adding this transaction will exceed your budget for {category}.")                                        
        except Exception as e:
            print(f"An error occurred while adding transaction: {e}")
        else:
            print("Transaction added successfully.")
        finally:
            print("Add transaction process completed.")
    def show_transactions(self):
        for t in self.transactions:
            print(t)
    def show_balance(self):
        income = sum (t.amount for t in self.transactions if t.t_type == "income")
        expense = sum (t.amount for t in self.transactions if t.t_type == "expense")
        balance = income - expense
        print(f"Current balance: {balance}")
        print(f"Total income: {income}")
        print(f"Total expense: {expense}")
        print(f"net balance: {balance}")
    def category_summary(self):
        expenses = [t for t in self.transactions if t.t_type == "expense"]
        summary = {}
        for t in expenses:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        store_summary = sorted(summary.items(), key=lambda x: x[1], reverse=True)
        print("\nCategory Summary: high to low")
        for cat, amt in store_summary:
            print(f"{cat}: {amt}")
    def save(self):
        save__to_file(self.transactions)
# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    tracker =FinanceTracker()
    while True:
        print("\n 1.Add transaction")
        print("2.Show transactions")
        print("3.Show balance")
        print("4.Category summary")
        print("5.Save and exit")
        choice = input("Choose an option: ")
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (food, salary, entertainment, other): ")
                description = input("Enter description: ")
                t_type = input("Enter type (income/expense): ")
                tracker.add_transaction(amount, category, description, t_type)
            except ValueError:
                print("Invalid input. Please enter a valid number for amount.")
        elif choice == "2":
            tracker.show_transactions()
        elif choice == "3":
            tracker.show_balance()
        elif choice == "4":
            tracker.category_summary()
        elif choice == "5":
            tracker.save()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



            



                    

