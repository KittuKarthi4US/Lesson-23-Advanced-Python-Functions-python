items = ["pencil", "eraser", "notebook", "pen", "glue"]
stock_count = [12, 0, 3, 5, 8]

inventory = {items:count for items, count in zip(items, stock_count)}
print(inventory)

instock_items = [item for item in items if inventory[item]>0]
print(instock_items)

chosen_item = input("What would you like to purchase :")

if chosen_item not in instock_items:
    print("Out of stock !")
    exit()

prices = [10, 50, 120, 30, 80]
markup_price = int(input("What is your markup price :"))

markedup_price = list(map(lambda p: p + markup_price, prices))
print(markedup_price)

index = items.index(chosen_item)
chosen_price = markup_price[index]
print(chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1
print('You have purchased the notebook , thank you')