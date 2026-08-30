from termcolor import colored
import json


TITLE = "===== EXPENSE TRACKER =====\n"

FEATURES_MENU = {
    1: "Add expense",
    2: "Delete expense",
    3: "Update expense",
    4: "List expenses",
    5: "Search expenses",
    6: "Filter by category",
    7: "Calculate total",
    8: "Save to JSON",
    9: "Load from JSON",
    10: "Exit"
}

CATEGORIES = {
    1: "Food",
    2: "Transportation",
    3: "Bills",
    4: "Entertainment",
    5: "Education"
}

MAIN_INPUT_COLOR1 = "white"
MAIN_INPUT_COLOR2 = "on_yellow"
TITLE_COLOR = "cyan"
INPUT_PROMPT_COLOR = "yellow"
SUCCESS_COLOR = "green"
ERRORS_COLOR = "red"


DATA_STORAGE = []


def show_menu_categories(title, menu, categories, title_color, permition=False):
    if not permition:
        print(colored(title, title_color))

        for key, value in menu.items():
            print(f"{key}. {value}")

    else:
        print(" ")
        for key, value in categories.items():
            print(f"{key}. {value}")


def add_expenses(title, menu, data_storage, categories, input_prompt_color, success_color, title_color, errors_color):
    data_dict = {}

    amount = int(input(colored("Enter amount: ", input_prompt_color)))
    description = input(
        colored("Enter expense description: ", input_prompt_color))

    show_menu_categories(title, menu, categories, title_color, permition=True)
    print("")
    category = int(
        input(colored("Choose a category (by the number): ", input_prompt_color)))

    if category in categories:

        data_dict["amount"] = amount
        data_dict["Description"] = description
        for key, item in categories.items():
            if category == key:
                data_dict["category"] = item

        data_storage.append(data_dict)

        print(colored("\nExpense successfully added.", success_color))
    else:
        print(colored("invalid category", errors_color))


def delete_expense(data_storage, title_color, input_prompt_color, success_color, errors_color):

    print(colored("===== EXPENSES =====\n", title_color))
    found = False
    if data_storage:
        for i, value in enumerate(data_storage, start=1):
            print(
                f"{i}.{value['Description']} | {value['category']} | ${value['amount']}")

        print("")

        delet_input = int(
            input(colored("Enter the expense number to delete: ", input_prompt_color)))

        for j, value in enumerate(data_storage.copy(), start=1):
            if delet_input == j:
                found = True
                data_storage.remove(value)
                break

        if not found:
            print(colored("Expense Not Found!", errors_color))
        if found:
            print(colored("\nExpense deleted successfully!\n", success_color))
    else:
        print(colored("No Expense Exists!", errors_color))


def update_expense(title, menu, categories, data_storage, input_prompt_color, success_color, errors_color, title_color):
    if data_storage:
        found = False

        for i, value in enumerate(data_storage, start=1):
            print(
                f"{i}.{value['Description']} | {value['category']} | ${value['amount']}")

        print(" ")

        update = int(
            input(colored("Enter expense number to update: ", input_prompt_color)))

        print(" ")

        for j, item in enumerate(data_storage, start=1):
            if update == j:
                found = True

                amount = int(
                    input(colored("Enter amount: ", input_prompt_color)))

                description = input(
                    colored("Enter expense description: ", input_prompt_color))

                show_menu_categories(
                    title, menu, categories, title_color, permition=True)

                print("")

                category = int(
                    input(colored("Choose a category (by the number): ", input_prompt_color)))

                if category in categories:
                    item['amount'] = amount
                    item['Description'] = description
                    item['category'] = categories[category]

                    print(colored("Expense updated successfully!", success_color))
                else:
                    print(
                        colored("Invalid category. Expense was not updated.", errors_color))

                break

        if not found:
            print(colored("Expense Not Found!", errors_color))

    else:
        print(colored("No Expense Exists!", errors_color))


def list_expenses(data_storage, title_color, errors_color):
    if data_storage:
        print(colored("===== EXPENSES =====\n", title_color))

        for i, expense in enumerate(data_storage, start=1):
            print(f"{i}. {expense['Description']}")
            print(f"   Amount: ${expense['amount']}")
            print(f"   Category: {expense['category']}")
            print(" ")
    else:
        print(colored("No Expenses Exists!", errors_color))


def search_expenses(data_storage, input_prompt_color, errors_color):
    if data_storage:
        search = input(colored("Search: ", input_prompt_color))
        print(" ")
        found = False

        for i, expense in enumerate(data_storage, start=1):
            if search.casefold() == expense['Description'].casefold() or search.casefold() in expense['Description'].casefold():
                found = True
                print(f"{i}. {expense['Description']}")
                print(f"   Amount: ${expense['amount']}")
                print(f"   Category: {expense['category']}")
                print(" ")

        if not found:
            print(colored("No Expenses Found.", errors_color))
    else:
        print(colored("No Expense Exists!", errors_color))


def filter_by_category(data_storage, categories, errors_color, input_prompt_color):
    for key, value in categories.items():
        print(f"{key}. {value}")

    print(" ")

    choos = int(input(colored("Choose a category: ", input_prompt_color)))

    print(" ")
    found = False
    if data_storage:

        for key, value in categories.items():
            if key == choos:
                for i, expense in enumerate(data_storage, start=1):
                    if expense['category'] == value:
                        found = True
                        print(f"{i}. {expense['Description']}")
                        print(f"   Amount: ${expense['amount']}")
                        print(f"   Category: {expense['category']}")
                        print(" ")

        if not found:
            print(colored("No Expenses Found.", errors_color))

    else:
        print(colored("No Expense Exists!", errors_color))


def calculate_total_expenses(data_storage):
    total_expenses = 0
    for expense in data_storage:
        total_expenses += expense['amount']

    print(f"Total Expenses: ${total_expenses}")


def save_expenses_to_json(data_storage, success_color):
    with open("expenses.json", "w") as file:
        json.dump(data_storage, file, indent=2)
        print(colored("Expenses saved successfully!", success_color))


def load_expenses_from_json(data_storage, success_color, errors_color):
    try:
        with open("expenses.json", "r") as file:
            data_storage = json.load(file)
            print(colored("Expenses loaded successfully!", success_color))

        return data_storage

    except FileNotFoundError:
        print(colored("json file doesn't exist", errors_color))
        return data_storage
    except json.JSONDecodeError:
        print(colored("invalid JSON", errors_color))
        return data_storage


def main(title, data_storage,  menu, categories, title_color, input_prompt_color, success_color, errors_color, main_input_color1, main_input_color2):

    show_menu_categories(title, menu, categories, title_color)

    while True:
        print(" ")
        select = int(
            input(colored("Choose an option:", main_input_color1, main_input_color2)))
        print(" ")

        if select == 1:
            add_expenses(title, menu, data_storage, categories,
                         input_prompt_color, success_color, title_color, errors_color)

        elif select == 2:
            delete_expense(data_storage, title_color,
                           input_prompt_color, success_color, errors_color)

        elif select == 3:
            update_expense(title, menu, categories, data_storage,
                           input_prompt_color, success_color, errors_color, title_color)

        elif select == 4:
            list_expenses(data_storage, title_color, errors_color)

        elif select == 5:
            search_expenses(data_storage, input_prompt_color, errors_color)

        elif select == 6:
            filter_by_category(data_storage, categories,
                               errors_color, input_prompt_color)

        elif select == 7:
            calculate_total_expenses(data_storage)

        elif select == 8:
            save_expenses_to_json(data_storage, success_color)

        elif select == 9:
            data_storage = load_expenses_from_json(
                data_storage, success_color, errors_color)

        elif select not in range(1, 11):
            print(colored("Invalid option.", errors_color))

        elif select == 10:
            break


main(TITLE, DATA_STORAGE, FEATURES_MENU, CATEGORIES, TITLE_COLOR, INPUT_PROMPT_COLOR,
     SUCCESS_COLOR, ERRORS_COLOR, MAIN_INPUT_COLOR1, MAIN_INPUT_COLOR2)
