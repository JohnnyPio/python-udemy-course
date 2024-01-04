from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_made = MoneyMachine()

coffee_machine = True
while coffee_machine:
    # Prompt a user which coffee they want
    user_choice = input(f"What coffee would you like? {menu.get_items()}.\n")

    # Turn off coffee machine by selecting off
    if user_choice == "off":
        coffee_machine = False
        print("Goodbye coffee...")
        break
    elif user_choice == "report":
        print(CoffeeMaker.report(coffee_maker))
    else:
        # Find drink in dict
        selected_drink = menu.find_drink(user_choice)

        # Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(selected_drink):
            # Check if payment is sufficient
            if money_made.make_payment(selected_drink.cost):
                coffee_maker.make_coffee(selected_drink)
                print(f"The total machine profit = {money_made.profit}")

