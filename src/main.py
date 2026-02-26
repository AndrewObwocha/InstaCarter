from models import LineItem
from services import call_instacart_api


def input_shopping_items() -> list[LineItem]:
    user_items: list[LineItem] = [] 
    try:
        num_items = int(input("Enter num of items: "))
        
        for i in range(num_items):
            item_name = input(f"Enter item {i + 1}'s full name: ")
            item_quantity = int(input(f"Enter item {i + 1}'s quantity: "))
            item_units = input(f"Enter item {i + 1}'s unit: ")
            
            user_items.append(LineItem(item_name, item_quantity, item_units))
            
        return user_items
        
    except ValueError as e:
        print(f"Input Error: {e}")
        return [] 


if __name__ == "__main__":
    items: list[LineItem] = input_shopping_items()
    if items:
        call_instacart_api(items)
    else:
        print("No items to send to Instacart.")
        