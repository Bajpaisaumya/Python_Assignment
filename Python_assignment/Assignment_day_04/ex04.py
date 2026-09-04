'''Assignment 4: Atomic E-Commerce Order Processor
Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products must be processed atomically: either the entire order completes successfully, or the entire transaction fails. If one item in the order is out of stock or is unrecognized, no stock should be deducted for any other item (rollback).

Problem Description
Define two custom exceptions:
ProductNotFoundError (raised when a product ID is not present in the catalog).
OutOfStockError (raised when the customer's ordered quantity exceeds the available stock).
Write a function process_order(catalog, order):
catalog is a dictionary containing product database records. Format:
catalog = {
    "P01": {"price": 100.0, "stock": 5},
    "P02": {"price": 50.0, "stock": 2}
}
order is a dictionary containing product IDs (keys) and quantities ordered (values). Format: {"P01": 2, "P02": 1}.
Validation Phase: Before modifying any inventory levels:
Check if all ordered keys exist in the catalog. If a product ID does not exist, raise ProductNotFoundError with message: "Product '<product_id>' not found in store catalog."
Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, raise OutOfStockError with message: "Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: <available_stock>."
Execution Phase: If (and only if) all products pass validation:
Deduct the ordered quantities from the stock numbers in the catalog dictionary.
Calculate and return the total cost of the order (float).
If an exception was raised during validation, the catalog must remain completely unchanged.'''
'''Assignment 4: Atomic E-Commerce Order Processor
Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products 
must be processed atomically: either the entire order completes successfully, or the entire 
transaction fails. If one item in the order is out of stock or is unrecognized, no stock 
should be deducted for any other item (rollback).'''


class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass
def process_order(catalog,order):
    for k,v in order.items():
        if k not in catalog:
            raise ProductNotFoundError(f"Product {k} is not found in catalog! ")
        stk=catalog[k]["stock"]
        if v>stk:
            raise OutOfStockError( f"Product '{k}' is out of stock. " f"Requested: {v}, Available: {stk}." )
    total=0.0
    for k,v in order.items(): 
        price = catalog[k]["price"] 
        if v<=stk :
         catalog[k]["stock"] -= v 
         total += price * v 
    return total
def main():
    catalog = {
    "P01": {"price": 100.0, "stock": 5},
    "P02": {"price": 50.0, "stock": 2}}
    order={"P01": 2, "P02": 1}
    try:
        total=process_order(catalog,order)
        print('Total Cost :',total)
        print('Updated Catalog :',catalog)
    except ProductNotFoundError as e:
        print(e)
    except OutOfStockError as e:
        print(e)
main()