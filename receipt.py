appetizer = int(input("How much did your appetizer cost?"))
entree = int(input("How much did your entree cost?"))
desert = int(input("How much did your desert cost?"))

cost = appetizer + entree + desert
print("The cost of your meal was", cost, "$")

payment = int(input("How much cash are you paying"))
change = payment - cost
print("Your change is", change)
