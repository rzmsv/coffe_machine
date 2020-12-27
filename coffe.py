# 1- report (water : 300 ml , milk : 200ml , coffe: 100g , money: $0)

# 2- make 3 hot flavours (espresso , latte , cappuccino)

# 3- detail : espresso : 50ml Water , 18g Coffe
#             Latte : 200ml Water , 24g Coffe , 150ml Milk
#             Cappucchino : 250ml Water , 24g Coffe ,100ml Milk

# 4- price : espresso : $1.50 , latte : $ 2.50 , cappuccino : 3.00


# START
MENU = {
    "espresso": {
          "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
coins = {
     "penny": 0.01,
     "dime": 0.10,
     "nickel": 0.05,
     "quarter": 0.25
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report (res):
     print(f"Water : {res['water']}ml\nMilk : {res['milk']}ml\nCoffee : {res['coffee']}g\nMoney : ${res['money']}")
# report(resources)


def giveCoin (coin):
     pen = int(input("how many pennies? "))
     di = int(input("how many dimes? "))
     nick = int(input("how many nickels? "))
     qua = int(input("how many quarters? "))
     return (pen * coin['penny'])+(di * coin['dime']) + (nick * coin['nickel']) + (qua * coin['quarter'])
# giveCoin(coins)


def flavours (menu,flavour):
     # resources = {}
     for f in menu:
          if flavour == f:
               res =  {
                    "water": resources["water"] - MENU[f]["ingredients"]["water"],
                    "milk": resources["milk"] - MENU[f]["ingredients"]["milk"],
                    "coffee": resources["coffee"] - MENU[f]["ingredients"]["coffee"],
                    "money": resources["money"] + MENU[f]["cost"]
               }
               return res

# print(flavours(MENU,resources))


while True :
     
     flavour = input("What would you like? (espresso/latte/cappuccino): ")
     if flavour == "report":
          report(resources)
     if flavour == "latte" or flavour == "espresso" or flavour == "cappuccino":
          coin = giveCoin(coins)
          # print(coin)
          # print(resources)
          if coin < MENU[flavour]["cost"]:
               print("Sorry that's not enough money. Money refunded.")
          if resources["milk"] < 0 :
               print(f"Sorry there is not enogh Milk .")
          if resources["coffee"] < 0:
               print(f"Sorry there is not enogh Coffee .")
          
          if coin > MENU[flavour]["cost"]:
               if resources["water"] - MENU[flavour]["ingredients"]["water"] >= 0:
                    resources = flavours(MENU,flavour)
                    print(f"Here is your {flavour} Enjoy!")
               else:
                    print(f"Sorry there is not enogh Water .")