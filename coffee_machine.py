# Write your code here
stock = {"water": 400, "milk": 540, "coffee": 120, "cups": 9, "money": 550}

def menu():
    while True:
        main_input = input("\nWrite action (buy, fill, take, remaining, exit):")
        if main_input == "buy":
            print()
            coffee_select()
        elif main_input == "fill":
            print()
            restock()
        elif main_input == "take":
            print()
            take()
        elif main_input == "remaining":
            print()
            show_stock()
        elif main_input == "exit":
            break


def restock():
    stock["water"] += int(input("Write how many ml of water do you want to add:"))
    stock["milk"] += int(input("Write how many ml of milk do you want to add:"))
    stock["coffee"] += int(input("Write how many grams of coffee beans do you want to add:"))
    stock["cups"] += int(input("Write how many disposable cups of coffee do you want to add:"))


def take():
    print("I gave you " + str(stock["money"]))
    stock["money"] -= stock["money"]


def show_stock():
    print("The coffee machine has:")
    print(str(stock["water"]) + " of water")
    print(str(stock["milk"]) + " of milk")
    print(str(stock["coffee"]) + " of coffee beans")
    print(str(stock["cups"]) + " of cups")
    print(str(stock["money"]) + " of money")


def make_espresso():
    recipe = {"water": 250, "coffee": 16, "cups": 1}
    money = 4
    ingredient_test = 0
    temp = stock.copy()
    for key in recipe:
        temp[key] -= recipe[key]
        if temp[key] < 0:
            ingredient_test += 1
            print("Sorry, not enough ", key, "!")
            break
    if ingredient_test == 0:
        stock["money"] += money
        print("I have enough resources, making you a coffee!")
        for key in recipe:
            stock[key] -= recipe[key]


def make_latte():
    recipe = {"water": 350, "milk": 75, "coffee": 20, "cups": 1}
    money = 7
    ingredient_test = 0
    temp = stock.copy()
    for key in recipe:
        temp[key] -= recipe[key]
        if temp[key] < 0:
            ingredient_test += 1
            print("Sorry, not enough ", key, "!")
            break
    if ingredient_test == 0:
        stock["money"] += money
        print("I have enough resources, making you a coffee!")
        for key in recipe:
            stock[key] -= recipe[key]


def make_cappucino():
    recipe = {"water": 200, "milk": 100, "coffee": 12, "cups": 1}
    money = 6
    ingredient_test = 0
    temp = stock.copy()
    for key in recipe:
        temp[key] -= recipe[key]
        if temp[key] < 0:
            ingredient_test += 1
            print("Sorry, not enough ", key, "!")
            break
    if ingredient_test == 0:
        stock["money"] += money
        print("I have enough resources, making you a coffee!")
        for key in recipe:
            stock[key] -= recipe[key]


def coffee_select():
    while True:
        selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if selection == "1":
            make_espresso()
            break
        elif selection == "2":
            make_latte()
            break
        elif selection == "3":
            make_cappucino()
            break
        elif selection == "back":
            break


menu()
