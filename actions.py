# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.palms.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print ("- " + store.name )

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    #user_input( "Which store would you like to shop at?")
    for store in stores:
        if store.lower() == store_name.lower():
            return True

        
    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
        #user_input = input("Pick a store by typing it's name or type checkout to exit: ")


    while True:
        user_input = input("Pick a store by typing it's name or type checkout to exit: ")

        for store in stores:
            if store.name.lower() == user_input.lower():
                #error was that store had no attribute lower. Store is not a string therefore it can not have lower. 
                # print(store.name)
                return store

        if user_input.lower() == "checkout":
            # print ("Thank you for visiting our site")
            return False

        print ("The store does not exist")

        user_input = input("Pick a store by typing it's name or type checkout to exit: ")





def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print ("-----------------------")

    print (picked_store.name + ": ")

    for products in picked_store.products:

     # for the products inside the array. The pciked stor ei sna object inside it is attributes. The attribute product has an array.
        print ("\t Product Name: "+ products.name)
        print ("\t Description: "+ products.description)
        print ("\t Price: "+ str(products.price))

        print ("\n")


    user_input = input("Pick the items you'd like to add in your cart by typing the product name exactly as it is was spelled above.\nType back to go back to the main menu where you can checkout. ")
    
    
    #while True:
    for products in picked_store.products:
            
        #issue was in need of user input again
            if user_input.lower() != "back":
                if user_input.lower() == products.name.lower():

                    cart.add_to_cart(products)
                #my error was that i added the user input and not the entire object (which includes all the information needed)
                    user_input = input()
                


            elif user_input.lower()!= products.name.lower():

                user_input = input ("This does not exist. Please type again: ")

            else:

                print ("You have chosen to go back!")
                break




def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    print_stores()
    picked_store = pick_store()
    pick_products(cart, picked_store)
    while True:

        user_input = input ("Pick a store by typing it's name or type checkout to pay your bills and say your goodbyes:\n")

        if user_input.lower() != "checkout":

            picked_store = pick_store()
            pick_products (cart, picked_store)

            return True

        else:
            print (cart.print_receipt())
            return False
    #your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
