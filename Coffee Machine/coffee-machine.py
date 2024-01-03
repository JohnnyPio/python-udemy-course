MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Variable setting
ingredients_str = "ingredients"
water_str = "water"
milk_str = "milk"
coffee_str = "coffee"

coffee_machine = True
while coffee_machine:
    # Prompt a user which coffee they want
    user_choice = input(f"What coffee would you like? (espresso/latte/cappuccino).\n")

    # Turn off coffee machine by selecting off
    if user_choice == "off":
        coffee_machine = False
        print("Goodbye coffee...")
        break

    # Print Report
    money_made = 0

    def report_print(res,money):
        print(f"Here is a coffee machine report! {res}")
        print(f"Here is how much money the machine has: {money}")

    if user_choice == "report":
        report_print(resources, money_made)

    if user_choice not in ["report", "off", "espresso", "latte", "cappuccino"]:
        print("Invalid selection, please choose again.\n")

    # Check if resources are sufficient
    def enough_resources(choice):
        if MENU[choice][ingredients_str][water_str] > resources[water_str]:
            print("Sorry there is not enough " + water_str)
            return False
        elif MENU[choice][ingredients_str][milk_str] > resources[milk_str]:
            print("Sorry there is not enough " + milk_str)
            return False
        elif MENU[choice][ingredients_str][coffee_str] > resources[coffee_str]:
            print("Sorry there is not enough " + coffee_str)
            return False
        else:
            print("Please insert coins!")
            return True

    # if not enough_resources(user_choice): ... something should re-prompt the user

    # Process coins
    print("Please insert coins.\n")
    quarters_inserted = int(input("How many quarters?: "))
    dimes_inserted = int(input("How many dimes?: "))
    nickels_inserted = int(input("How many nickels?: "))
    pennies_inserted = int(input("How many pennies?: "))

    money_payed = quarters_inserted * 0.25 + dimes_inserted * 0.10 + nickels_inserted * 0.05 + pennies_inserted * 0.01
    print(f"Total money paid: {money_payed}")

# Check if transaction is successful
    def transaction_successful(payed,cost):
        if payed > cost:
            change = round(payed - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        elif payed == cost:
            print(f"Thank you for using exact change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

# Make Coffee
    if transaction_successful(money_payed, MENU[user_choice]["cost"]):
        # Update how much money machine has
        money_made += money_payed

        # TODO FIX Update resources dict
        resources[water_str] = resources[water_str] - MENU[user_choice][ingredients_str][water_str]
        resources[milk_str] = resources[milk_str] - MENU[user_choice][ingredients_str][milk_str]
        resources[coffee_str] = resources[coffee_str] - MENU[user_choice][ingredients_str][coffee_str]

        report_print(resources, money_made)
        print(f"Here is your {user_choice}, enjoy!")
