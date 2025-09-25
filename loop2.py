"""largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)"""

menu_options = ["Add Item", "View Items", "Delete Item", "Exit"]

print("Main Menu")
for i, option in enumerate(menu_options, start=1):
    print(f"{i}. {option}")

choice = input("Enter your choice (1-4): ")
