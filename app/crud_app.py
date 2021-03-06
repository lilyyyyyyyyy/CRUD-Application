def enlarge(i):
    return i * 100




import csv

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

def map_id(product): return int(product["id"])
def auto_increment_id(products):
    product_ids = list(map(map_id, products))
    if len(product_ids) == 0: next_id = 1
    else: next_id = max(product_ids) + 1
    return next_id


menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------
Welcome @lilyyyyyyyyy!
There are {0} products in the database. Please select an operation:
    operation | description
    --------- |------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
 """.format(len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

# example_new_product = {"id": 100, "name": "New Item", "aisle": "snacks", "department": "snacks", "price": 1.99}
# products.append(example_new_product)


# other_path = "/Users/lily/Desktop/CRUD-Application/data/copy_products.csv"
# with open(other_path, "w") as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
#     writer.writeheader()
#     for product in products:
#         writer.writerow(product)



def list_product():
    print("THERE ARE {0} PRODUCTS: ".format(len(products)))
    for product in products:
        print(" + ", dict(product))

def show_product():
    choose_a_product = input("OK. Please specify the product's identifier: ")
    product = [p for p in products if p["id"] == choose_a_product]
    if len(product)>0:
        product = product[0]
        print("SHOWING A PRODUCT HERE!")
        print(dict(product))
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", choose_a_product)

def create_product():
    print("OK. Please specify the product's information...")
    product_name = input("name: ")
    product_aisle = input("aisle: ")
    product_department = input("department: ")
    product_price = input("price: ")
    new_product = {
        "id": auto_increment_id(products),
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("CREATING A PRODUCT HERE!")
    print(new_product)
    products.append(new_product)


def update_product():
    choose_a_product = input("OK. Please specify the product's identifier: ")
    product = [p for p in products if p["id"] == choose_a_product]
    if len(product)>0:
        product = product[0]
        print("OK. Please specify the product's information..." )
        product['name'] = input("Change name from {0} to: " .format(product['name']))
        product['aisle'] = input("Change aisle from {0} to: " .format(product['aisle']))
        product['department'] = input("Change department from {0} to: " .format(product['department']))
        product['price'] = input("Change price from {0} to: " .format(product['price']))
        print("UPDATING A PRODUCT HERE!")
        print(dict(product))
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", choose_a_product)

def destroy_product():
    choose_a_product = input("OK. Please specify the product's identifier: ")
    product = [p for p in products if p["id"] == choose_a_product][0]
    if product:
        print("DESTROYING PRODUCT HERE!")
        print(dict(product))
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", choose_a_product)


if chosen_operation == "List": list_product()
elif chosen_operation == "Show":
    show_product()
elif chosen_operation == "Create":
    create_product()
elif chosen_operation == "Update":
    update_product()
elif chosen_operation == "Destroy":
    destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

# WRITE PRODUCTS TO FILE

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)
