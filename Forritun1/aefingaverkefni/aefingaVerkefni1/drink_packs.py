drinkpack_size = int(input("How big is the drink pack?: "))
desired_amount = int(input("How many are you going to buy?: "))

amount_of_packs = desired_amount // drinkpack_size
seperate_drinks = desired_amount % drinkpack_size

print("You have to buy {} packs and {} seperate".format(amount_of_packs, seperate_drinks))