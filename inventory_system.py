# import json
# import logging
# from datetime import datetime

# # Global variable
# stock_data = {}

# def addItem(item="default", qty=0, logs=[]):
#     if not item:
#         return
#     stock_data[item] = stock_data.get(item, 0) + qty
#     logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

# def removeItem(item, qty):
#     try:
#         stock_data[item] -= qty
#         if stock_data[item] <= 0:
#             del stock_data[item]
#     except:
#         pass

# def getQty(item):
#     return stock_data[item]

# def loadData(file="inventory.json"):
#     f = open(file, "r")
#     global stock_data
#     stock_data = json.loads(f.read())
#     f.close()

# def saveData(file="inventory.json"):
#     f = open(file, "w")
#     f.write(json.dumps(stock_data))
#     f.close()

# def printData():
#     print("Items Report")
#     for i in stock_data:
#         print(i, "->", stock_data[i])

# def checkLowItems(threshold=5):
#     result = []
#     for i in stock_data:
#         if stock_data[i] < threshold:
#             result.append(i)
#     return result

# def main():
#     addItem("apple", 10)
#     addItem("banana", -2)
#     addItem(123, "ten")  # invalid types, no check
#     removeItem("apple", 3)
#     removeItem("orange", 1)
#     print("Apple stock:", getQty("apple"))
#     print("Low items:", checkLowItems())
#     saveData()
#     loadData()
#     printData()
#     eval("print('eval used')")  # dangerous

# main()



"""
Inventory system – simple in-memory stock tracker.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# --------------------------------------------------------------------------- #
# Logging configuration (used later)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global stock dictionary
stock_data: Dict[str, int] = {}


def add_item(
    item: str = "default",
    qty: int = 0,
    logs: Optional[List[str]] = None,
) -> None:
    """Add *qty* units of *item* to the stock.

    Args:
        item: Name of the item (must be a string).
        qty: Quantity to add (positive or negative).
        logs: Optional list that receives a log line for each call.
    """
    if logs is None:
        logs = []

    if not item or not isinstance(item, str):
        logging.warning(f"Invalid item name: {item!r}")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    msg = f"Added {qty} of {item}"
    logs.append(f"{datetime.now()} - {msg}")
    logging.info(msg)


def remove_item(item: str, qty: int) -> None:
    """Remove *qty* units of *item*. Delete entry if <= 0."""
    try:
        if item not in stock_data:
            logging.warning(f"Cannot remove {qty} of {item}: not in stock")
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info(f"Removed {item} from stock (qty <= 0)")
    except KeyError:
        logging.error(f"KeyError while removing {item}")


def get_qty(item: str) -> int:
    """Return current quantity (0 if missing)."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load stock dictionary from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data = {str(k): int(v) for k, v in data.items()}
        logging.info(f"Loaded data from {file}")
    except FileNotFoundError:
        logging.warning(f"{file} not found – starting empty")
    except json.JSONDecodeError as exc:
        logging.error(f"Invalid JSON in {file}: {exc}")


def save_data(file: str = "inventory.json") -> None:
    """Persist stock dictionary to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
        logging.info(f"Saved data to {file}")
    except Exception as exc:   # broad but logged – OK for tiny demo
        logging.error(f"Failed to save {file}: {exc}")


def print_data() -> None:
    """Pretty-print the current inventory."""
    print("\n=== Items Report ===")
    if not stock_data:
        print("  (empty)")
    else:
        for itm, q in sorted(stock_data.items()):
            print(f"  {itm} -> {q}")
    print("====================\n")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of items below *threshold*."""
    return [i for i, q in stock_data.items() if q < threshold]


def main() -> None:
    """Demo / test driver."""
    log_lines: List[str] = []

    add_item("apple", 10, log_lines)
    add_item("banana", -2, log_lines)
    # add_item(123, "ten")   # <-- removed – invalid types

    remove_item("apple", 3)
    remove_item("orange", 1)   # not present → logged warning

    logging.info(f"Apple stock: {get_qty('apple')}")
    logging.info(f"Low items (<5): {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Show the log that was collected
    print("=== Action Log ===")
    for line in log_lines:
        print(line)
    print("==================\n")


if __name__ == "__main__":
    main()