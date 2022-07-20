# Write your code here
money = 550
water = 400
milk = 540
beans = 120
cups = 9

class CoffeeMachine:
    
    def __init__(self, action):
        self.action = action
        self.state = "Choosing an action"
        
    def choose_action(self):
        if self.action == '1':
            self.state = "Preparing a espresso"
            espresso()
        elif self.action == '2':
            self.state = "Preparing a latte"
            latte()
        elif self.action == '3':
            self.state = "Preparing a cappuccino"
            cappuccino()            
        elif self.action == 'fill':
            self.state = "Filling supplies"
            fill()
        elif self.action == 'take':
            self.state = "Taking the money"
            take()
        elif self.action == 'remaining':
            self.state = "Showing supplies"
            print_state()
            
def print_state():
    global water
    global milk
    global beans
    global cups
    global money
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")
    
def espresso():
    global water
    global beans
    global cups
    global money
    if water >= 250:
        if beans >= 16:
            if cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
            else:
                print("Sorry, not enough cups!")
                main()
        else:
            print("Sorry, not enough beans!")
            main()
    else:
        print("Sorry, not enough water!")
        main()
    
def latte():
    global water
    global milk
    global beans
    global cups
    global money
    if water >= 350:
        if milk >= 75:
            if beans >= 20:
                if cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 350
                    milk -= 75
                    beans -= 20
                    cups -= 1
                    money += 7
                    main()
                else:
                    print("Sorry, not enough cups!")
                    main()
            else:
                print("Sorry, not enough beans!")
                main()
        else:
            print("Sorry, not enough milk!")
            main()
    else:
        print("Sorry, not enough water!")
        main()
                    
def cappuccino():
    global water
    global milk
    global beans
    global cups
    global money
    if water >= 200:
        if milk >= 100:
            if beans >= 12:
                if cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 200
                    milk -= 100
                    beans -= 12
                    cups -= 1
                    money += 6
                    main()
                else:
                    print("Sorry, not enough cups!")
                    main()
            else:
                print("Sorry, not enough beans!")
                main()
        else:
            print("Sorry, not enough milk!")
            main()
    else:
        print("Sorry, not enough water!")
        main()

def take():
    global money
    print("I gave you $" + str(money))
    money = 0

def fill():
    global water
    global milk
    global beans
    global cups
    added_water = int(input("Write how many ml of water do you want to add: "))
    added_milk = int(input("Write how many ml of milk do you want to add: "))
    added_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
    added_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += added_water
    milk += added_milk
    beans += added_coffee
    cups += added_cups

def main():
    while True:
        try:
            accion = input("Write action (buy, fill, take, remaining, exit):")
            if accion == 'buy':
                cafe_seleccionado = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if cafe_seleccionado == '1':
                    cafetera = CoffeeMachine(cafe_seleccionado)
                    cafetera.choose_action()
                elif cafe_seleccionado == '2':
                    cafetera = CoffeeMachine(cafe_seleccionado)
                    cafetera.choose_action()
                elif cafe_seleccionado == '3':
                    cafetera = CoffeeMachine(cafe_seleccionado)
                    cafetera.choose_action()
                elif cafe_seleccionado == 'back':
                    main()
                else:
                    print("Invalid option!")
                    main()
            elif accion == 'take':
                cafetera = CoffeeMachine(accion)
                cafetera.choose_action()
            elif accion == 'fill':
                cafetera = CoffeeMachine(accion)
                cafetera.choose_action()
            elif accion == 'remaining':
                cafetera = CoffeeMachine(accion)
                cafetera.choose_action()
            elif accion == 'exit':
                break
            else:
                print("Invalid action!")
                break
        except EOFError:
            print ("EOFError")
            break

main()
