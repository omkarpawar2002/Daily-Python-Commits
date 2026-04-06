"""Mini Project – Shopping List Manager

Program manages shopping items.

Features:

add item
remove item
show list
update list

Concepts used:

list
append
remove
loops
conditions

Real life example:
manage grocery items."""


grocery_items = []
while True:
    choice = int(input("**GROCERY PRODUCT**"\
                       "\n 1.ADD ITEM "\
                       "\n 2.SHOW ITEM "\
                       "\n 3.UPDATE ITEM "\
                       "\n 4.DELETE ITEM "\
                       "\n 5.SHOW LIST ITEMS "\
                       "\n 6.EXIT "\
                       "\n ENTER YOUR CHOICE : "))
    if(choice == 1):
        num = int(input("How many items want to add to grocery : "))
        for i in range(num):
            item = input("Enter product name : ")
            grocery_items.append(item)
    elif(choice == 2):
        item = input("Enter product name : ")
        if(item in grocery_items):
            print("=====================")
            print(item,"is present in list")
            print("=====================")
        else:
            print("=====================")
            print(item,"is not present in list")
            print("=====================")
    elif(choice == 3):
        product = input("Enter product name you want to update : ")
        if(product in grocery_items):
            product_index = grocery_items.index(product)
            new_product_name = input("Enter new product name : ")
            grocery_items[product_index] = new_product_name
        else:
            print("=====================")
            print("Product Is Not present")
            print("=====================")
    elif(choice == 4):
        product = input("Enter product name you want to delete : ")
        if(product in grocery_items):
            grocery_items.remove(product)
        else:
            print("=====================")
            print("Product Is Not present")
            print("=====================")
    elif(choice == 5):
        print("=====================")
        print("Grocery Items : ",grocery_items)
        print("=====================")
    elif(choice == 6):
        break
    else:
        print("=====================")
        print("Incorrect choice")
        print("=====================")