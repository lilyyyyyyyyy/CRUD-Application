import csv

products = []

csv_file_path = "/Users/lily/Desktop/CRUD-Application/data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print(products)


# menu = """
# -----------------------------------
# PRODUCTS APPLICATION
# -----------------------------------
# Welcome @lilyyyyyyyyy!
# There are 20 products in the database. Please select an operation:
#     operation | description
#     --------- |------------------
#     'List'    | Display a list of product identifiers and names.
#     'Show'    | Show information about a product.
#     'Create'  | Add a new product.
#     'Update'  | Edit an existing product.
#     'Destroy' | Delete an existing product.
#  """
#
# chosen_operation = input(menu)
# chosen_operation = chosen_operation.title()
#
# def list_product():
#     print("List")
# def show_product():
#     print("Show")
# def create_product():
#     print("Create")
# def update_product():
#     print("Update")
# def destroy_product():
#     print("Destroy")
#
#
# if chosen_operation == "List":
#     list_product()
# elif chosen_operation == "Show":
#     show_product()
# elif chosen_operation == "Create":
#     create_product()
# elif chosen_operation == "Update":
#     update_product()
# elif chosen_operation == "Destroy":
#     destroy_product()
# else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
