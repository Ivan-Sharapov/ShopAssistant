import datetime
import os

INITIAL_STOCK = 1000
STOCK_FILE = "stock.txt"
PRICE_PER_ITEM = 2

def init_stock_file():
    """Creates stock file if it doesn't exist"""
    if not os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, "w", encoding="utf-8") as f:
            f.write(str(INITIAL_STOCK))

def get_current_stock():
    """Returns current inventory count"""
    init_stock_file()
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except (ValueError, PermissionError):
        return INITIAL_STOCK

def update_stock(quantity_sold):
    """Updates inventory after sale"""
    current = get_current_stock()
    new_stock = current - quantity_sold
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        f.write(str(max(new_stock, 0)))  

def save_sale(quantity):
    """Records sale details"""
    revenue = quantity * PRICE_PER_ITEM
    tax = revenue * 0.20
    net_profit = revenue - tax
    
    with open("sales.txt", "a", encoding="utf-8") as f:
        f.write(
            f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Sold: {quantity} units\n"
            f"Remaining stock: {get_current_stock() - quantity}\n"
            f"Revenue: ${revenue:.2f}\n"
            f"Tax (20%): ${tax:.2f}\n"
            f"Net profit: ${net_profit:.2f}\n"
            f"{'-'*40}\n"
        )
    update_stock(quantity)

def save_feedback(rating, feedback=None):
    """Saves customer feedback"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Rating: {rating}/5\n")
        if feedback:
            f.write(f"[{timestamp}] Review: {feedback}\n")
        f.write(f"{'-'*40}\n")

current_stock = get_current_stock()

dollars = int(input("Enter your budget in dollars: "))
cents = int(input('Enter your budget in cents: '))
budget = dollars + cents / 100

affordable_quantity = budget // PRICE_PER_ITEM
available_quantity = int(min(affordable_quantity, current_stock))

if available_quantity <= 0:
    print('\nWe cannot offer you anything')
    print('Goodbye')
else:
    print(f'\nCurrent stock: {current_stock} units')
    print(f'You can purchase up to {available_quantity} units')
    
    while True:
        try:
            show_catalog = int(input('View product catalog? (1-Yes, 0-No): '))
            if show_catalog in (0, 1):
                break
            else:
                print("Error: Enter 0 or 1 only!")
        except ValueError:
            print("Error: Enter a number!")

    if show_catalog == 1:
        print("\nAvailable products:\n1. Electronics\n2. Clothing\n3. Groceries\n")

while True:
    try:
        purchase_quantity = int(input('Enter quantity to purchase: '))
        if purchase_quantity < 0:
            print("Error: Quantity cannot be negative!")
        elif purchase_quantity > current_stock:
            print(f"Error: Only {current_stock} units available!")
        else:
            break
    except ValueError:
        print("Error: Enter a whole number!")

remaining_balance = budget - purchase_quantity * PRICE_PER_ITEM

if remaining_balance < 0:
    print('\nInsufficient funds!')
    print(f'Maximum available: {available_quantity} units')
    
    while True:
        try:
            proceed = int(input('Purchase available quantity? (1-Yes, 0-No): '))
            if proceed in (0, 1):
                break
            else:
                print("Error: Enter 0 or 1!")
        except ValueError:
            print("Error: Enter a number!")
    
    if proceed == 1:
        total_cost = available_quantity * PRICE_PER_ITEM
        remaining = budget - total_cost
        print(f'\nPurchased: {available_quantity} units. Remaining balance: ${remaining:.2f}')
        save_sale(available_quantity)
    else:
        print('\nGoodbye!')
else:
    print(f'\nPurchase successful! Remaining balance: ${remaining_balance:.2f}')
    save_sale(purchase_quantity)

print("\n" + "="*40)
while True:
    try:
        stars = int(input("Rate our store (1-5 stars): "))
        if 1 <= stars <= 5:
            break
        else:
            print("Error: Enter 1-5 only!")
    except ValueError:
        print("Error: Enter a number!")

review = None
while True:
    try:
        leave_review = int(input("Leave text review? (1-Yes, 0-No): "))
        if leave_review in (0, 1):
            break
        else:
            print("Error: Enter 0 or 1!")
    except ValueError:
        print("Error: Enter a number!")

if leave_review == 1:
    review = input("Enter your review: ")

save_feedback(stars, review)
print("\nThank you for your rating!")
print("See you again!")
