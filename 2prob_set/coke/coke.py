coins = {
    "25 cents" : "25",
    "10 cents" : "10",
    "5 cents" : "5",
}

amount_due = 50
change_owed = 0

 # do i need to addd if user_input in coins.keys():
        #inserted_coin = coins[user_input]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    user_input = int(input("Insert Coin: "))
    if user_input != 0 and user_input == 25 or user_input == 10 or user_input == 5:
        amount_due = amount_due - user_input
    if amount_due <= 0:
        change_owed = amount_due * -1
        print(f"Change Owed: {change_owed}")
        break



