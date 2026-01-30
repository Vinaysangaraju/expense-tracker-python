class Expense:
    def __init__(self, amount, category, notes = None):
        self.amount = amount
        self.category = category
        self.notes = notes

class TrackerExpenses:
    def __init__(self):
        self.expenses = []
    def add_expenses(self, expense):
        self.expenses.append(expense)
    def display_expense(self):
        print("---- Expense List ----")
        for exp in self.expenses:
            print(f" -> Amount : {exp.amount}\n -> Category : {exp.category}\n -> Note : {exp.notes}\n")

tracker = TrackerExpenses()

while True:
    print("\n---- Expense Tracker ----\n")
    print("1. Add Expense ")
    print("2. View Expense ")
    print("3. Exit ")

    choice = input("Enter Your choice : ")
    if choice == "1":
        while True:
            try:
                amount = int(input("Enter Amount : "))
                if amount <= 0:
                    print("invalid Try again")
                else: 
                    break
            except ValueError:
                print("Enter Valid Value!")

        category = input("Enter Category : ")
        notes = input("Enter Note (Optional) : ")
        
        expense = Expense(amount, category, notes)
        tracker.add_expenses(expense)
        print("Expense is added Successfully :)")

    elif choice == "2":
        tracker.display_expense()

    elif choice == "3":
        print(" Exiting Program . . .")
        break

    else:
        print("Option Inavlid! Try again")
