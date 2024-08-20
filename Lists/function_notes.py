def say_hello():
    print("hello")
say_hello()

def say_goodbye():
    print("goodbye")
say_goodbye()

def say_something(something):
    print(f"{something}")

say_something("noodles")
say_something(1234)

def cash_withdrawal(amount,acc_num):
    print(f"withdrawing {amount} from account number: {acc_num}")

    cash_withdrawal(200, 12345678)
    cash_withdrawal(30, 987654321)

def coffee_order(size,drink):
        print(f"you have ordered size {size} drink: {drink}")

coffee_order("medium","lattee")
coffee_order("large","tea")

# Activity 1 - week 4 Functions


def birthday(name):
     print(f"happy birthday to you, happy birthday to you, happy birthday dear {name}")

birthday ("Amanda")

# Activity 2 - week 4 Functions

order_count = 0

def take_order(topping):
     global order_count
     print("Pizza with {}".format(topping))
     order_count += 1

take_order("pineapple","1")
take_order("ham","2")













   



