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


coffee_machine_status = "off"
global total_money
total_money = 0


def print_report():

    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : {total_money}")

    return


def resource_sufficient(user_choice):
    print(user_choice)

    if user_choice == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"] and \
                resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
            return True
    elif user_choice == "latte":
        if resources["water"] > MENU["latte"]["ingredients"]["water"] and \
                resources["milk"] > MENU["latte"]["ingredients"]["milk"] \
                    and resources["coffee"] > MENU["latte"]["ingredients"]["coffee"]:
            return True
    elif user_choice == "cappuccino":
        if resources["water"] > MENU["cappuccino"]["ingredients"]["water"] and \
                resources["milk"] > MENU["cappuccino"]["ingredients"]["milk"] \
                    and resources["coffee"] > MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
    else:
        return False


def process_coins(user_choice):

    sufficient_resources=resource_sufficient(user_choice)
    print("Please insert coins. ")
    qrt = int(input("Quarter."))
    dme = int(input("Dime."))
    nic = int(input("Nickel."))
    pen = int(input("Pennies."))

    total = 0.25*qrt + .1*dme + .05*nic + .01*pen
    print(f"total {total}")
    return total


def check_transaction(user_choice):

    total = process_coins(user_choice)
    global total_money
    if user_choice == "espresso" and total >= MENU["espresso"]["cost"] and resource_sufficient(user_choice):
        print("Enjoy your coffee.")
        total_money += total
        if total > MENU["espresso"]["cost"]:
            extra_change = total - MENU["espresso"]["cost"]
            print (f"Your coffee cost $ {MENU['espresso']['cost']}")
            print(f"Here is {extra_change} dollars in change.")
        else:
            print("Sorry that\'s not enough money. Money refunded.")

    if user_choice == "latte" and total >= MENU["latte"]["cost"] and resource_sufficient(user_choice):
        print("Enjoy your coffee.")
        total_money += total
        if total > MENU["latte"]["cost"]:
            extra_change = total - MENU["latte"]["cost"]
            print(f"Here is {extra_change} dollars in change.")
        else:
            print("Sorry that\'s not enough money. Money refunded.")

    if user_choice == "cappuccino" and total >= MENU["cappuccino"]["cost"] and resource_sufficient(user_choice):
        print("Enjoy your coffee.")
        total_money += total
        if total > MENU["cappuccino"]["cost"]:
            extra_change = total - MENU["cappuccino"]["cost"]
            print(f"Here is {extra_change} dollars in change.")
        else:
            print("Sorry that\'s not enough money. Money refunded.")


print(resources)
user_choice = input("What would you like?(espresso/latte/cappuccino):")
print_report()

if resource_sufficient(user_choice):
    check_transaction(user_choice)
    if user_choice == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        print(resources["water"])
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(resources["coffee"])
    elif user_choice == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        print(resources["water"])
        resources["milk"] -= MENU["latte"]["ingredients"]["milk "]
        print(resources["water"])
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print(resources["coffee"])

print(resources)
print(f"total {total_money}")
















