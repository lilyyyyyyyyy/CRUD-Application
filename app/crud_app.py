import csv

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

import csv

products = []

csv_file_path = "/Users/lily/Desktop/CRUD-Application/data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)


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
    print("Show")
def create_product():
    print("Create")
def update_product():
    print("Update")
def destroy_product():
    print("Destroy")


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
