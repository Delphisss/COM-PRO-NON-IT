total_items = 100
ordered_items = int(input("Enter the number of items to be taken out: "))

enough_items = ordered_items <= total_items

if not enough_items:
    print("There aren't enough items.")
else:
    remaining_items = total_items - ordered_items

if remaining_items < total_items * 0.5:
    items_to_fill = total_items - remaining_items
    print(f"Please fill inventory with {items_to_fill} more items.")
else:
    print("No need to fill inventory at this time.")

print(f"Remaining items in inventory: {remaining_items}")

# print(total_items)
