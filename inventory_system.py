import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item=None, qty=0, logs=None):
    """Add an item to the stock."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid data types for item or quantity.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    try:
        if not isinstance(item, str) or not isinstance(qty, int):
            raise ValueError("Invalid data types.")
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Tried to remove an item not in stock.")
    except Exception as e:
        logging.error(f"Error removing item: {e}")


def get_qty(item):
    """Get current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load stock data from file."""
    global stock_data
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        logging.warning("Inventory file not found. Starting fresh.")
        stock_data = {}


def save_data(file_name="inventory.json"):
    """Save stock data to file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file)


def print_data():
    """Display all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
