import questionary
from budget import Budget
# from analyze import Analysis
from db import DB


def cli():
    """
    The Command-Line Interface.

    :return: None
    """
    # The "main.py" database, to which you are connecting.
    db = DB.get_db()
    # Asks the user whether is he ready?
    if not questionary.confirm("Are you ready?").ask():
        quit()
    # Boolean variable is needed to stop the program loop if user chooses "Exit".
    stop = False
    # The program loop.
    while not stop:
        # The user is given a choice of actions.
        choice = questionary.select(
            "What do you want to do?",
            choices=["Enter", "Delete", "Start a new month", "Analyse", "Exit"]
        ).ask()

        if choice == "Enter":
            print("Important: Please enter the date in format YYYY-MM-DD")
            date = questionary.text("Please enter the date!").ask()
            income = (questionary.text("Please enter the income!\nJust press enter, or write 0 if no income!").ask())
            if income and income != 0:
                income_category = str(questionary.text("Please enter the income category (i.e. salary, bonus, etc.)!\n"
                                                       "Just press enter if no income category!").ask()).lower()
            else:
                income_category = None
            expense = (questionary.text("Please enter the expense!\nJust press enter, or write 0 if no "
                                        "expenses!").ask())
            if expense and expense != 0:
                expense_category = str(questionary.text("Please enter the expense category (i.e. food, pleasure, etc.)!"
                                                        "\nJust press enter if no expense category!").ask()).lower()
            else:
                expense_category = None
            if not income:
                income = .0
            if not expense:
                expense = .0
            try:
                Budget.data_entry(db, date, income, income_category, expense, expense_category)
            except PermissionError:
                print("Hm! It seems you haven't closed the Excel file!")
        if choice == "Delete":
            print("Important: Please enter the date in format YYYY-MM-DD")
            date = questionary.text("Please enter the date!").ask()
            income = questionary.confirm("Do you want to delete the income?").ask()
            expense = questionary.confirm("Do you want to delete the expenses?").ask()
            try:
                Budget.data_drop(db, date, income, expense)
            except PermissionError:
                print("Hm! It seems you haven't closed the Excel file!")
        if choice == "Start a new month":
            current_year = int(questionary.text("Please enter the year.").ask())
            current_month = int(questionary.text("Please enter the month.\n(i.e. January = 1, December = 12)").ask())
            try:
                Budget.new_month(db, current_year, current_month)
            except PermissionError:
                print("Hm! It seems you haven't closed the Excel file!")
        if choice == "Exit":
            # If the user chooses "Exit", program closes the CLI.
            # The program prints "Bye!".
            print("Bye!")
            # The program changes the stop value to True, in order to stop the program loop.
            stop = True


# Executed when invoked directly.
if __name__ == "__main__":
    # Calls the cli() method.
    cli()
