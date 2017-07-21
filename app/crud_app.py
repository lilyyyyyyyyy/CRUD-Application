menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------
Welcome @lilyyyyyyyyy!
There are 20 products in the database. Please select an operation:
    operation | description
    --------- |------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
 """

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

if chosen_operation == "List":
    print("List")
elif chosen_operation == "Show":
    print("Show")
elif chosen_operation == "Create":
    print("Create")
elif chosen_operation == "Update":
    print("Update")
elif chosen_operation == "Destroy":
    print("Destroy")
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
