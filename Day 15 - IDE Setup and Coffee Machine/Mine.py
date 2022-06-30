MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# TODO: 2. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): - DONE

# TODO: 7. Turn off the Coffee Machine by entering “ off ” to the prompt. -> after making 1 drink, ask user if want another. if NO, then turn off



# TODO: 3. Check resources sufficient? When user chooses drink

# TODO: 4. Process coins.

# TODO: 5. Check transaction successful?

# TODO: 6. Make Coffee.

# TODO: 1. Print report. - DONE

def choose_drink():
    global question
    question = input("Hi there. What would you like to drink? espresso/latte/cappuccino?: ")
    return

def coin_check():
    global total
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round((quarters * coins["quarters"]) + (dimes * coins["dimes"]) + (nickles * coins["nickles"]) + (pennies * coins["pennies"]),2)
    print(f"You have inserted ${total}.")
    return total

def report():
    print("Here is the report.")
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : ${resources['money']}")
    return
coffee_machine_on = True

while coffee_machine_on:
    choose_drink()
    if question == "report":
            report()
    elif question == "off".lower():
        coffee_machine_on = False
    elif question == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            print(f'All ingredients sufficient. Ready to make {question}.')
            print(f'Your {question} costs ${MENU["espresso"]["cost"]}. Please insert coins.')
            coin_check()
            if total < MENU["espresso"]["cost"]:
                print("Sorry. That's not enough money. Money refunded")
            elif total >= MENU["espresso"]["cost"]:
                resources["money"] += MENU["espresso"]["cost"]
                refund = round((total - MENU["espresso"]["cost"]),2)
                print(f"Here is ${refund} in change.")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources['coffee'] - MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is your {question}. Enjoy!")
        else:
            print('Insufficient ingredients. Choose another drink.')
    elif question == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            print(f'All ingredients sufficient. Ready to make {question}.')
            print(f'Your {question} costs {MENU["latte"]["cost"]}. Please insert coins.')
            coin_check()
            if total < MENU["latte"]["cost"]:
                print("Sorry. That's not enough money. Money refunded")
            elif total >= MENU["latte"]["cost"]:
                resources["money"] += MENU["latte"]["cost"]
                refund = round((total - MENU["latte"]["cost"]),2)
                print(f"Here is ${refund} in change.")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] = resources['coffee'] - MENU["latte"]["ingredients"]["coffee"]
                print(f"Here is your {question}. Enjoy!")
        else:
            print('Insufficient ingredients. Choose another drink.')
    elif question == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            print(f'All ingredients sufficient. Ready to make {question}.')
            print(f'Your {question} costs {MENU["cappuccino"]["cost"]}. Please insert coins.')
            coin_check()
            if total < MENU["cappuccino"]["cost"]:
                print("Sorry. That's not enough money. Money refunded")
            elif total >= MENU["cappuccino"]["cost"]:
                resources["money"] += MENU["cappuccino"]["cost"]
                refund = round((total - MENU["latte"]["cost"]),2)
                print(f"Here is ${refund} in change.")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] = resources['coffee'] - MENU["cappuccino"]["ingredients"]["coffee"]
                print(f"Here is your {question}. Enjoy!")
        else:
            print('Insufficient ingredients. Choose another drink.')