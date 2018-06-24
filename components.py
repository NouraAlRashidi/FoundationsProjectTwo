# CLASSES AND METHODS
class Store():
    
    
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []


    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
    

        self.products.append(product)
        #self.prodcuts.append (product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for product in self.products:
            print ("- " + products + "\n")


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price


    def __str__(self):
        # your code goes here!
        return self.name
    
class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)
        #After checking that the product exists in store, it will take all the information of that product and store it in the empty list above
        #Hence, the name, description and price is already within Class Cart

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for product in self.products:
            get_price = product.price

            #get_price = Product(products,"",)  
            #its creating a new product          
            total += get_price

        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print ("Here is your receipt")
        for product in self.products:
            print ("- " + product + "\n")
            #print ("\t Product Name: "+ products.name)
            #print ("\t Description: "+ products.description)
            #print ("\t Price: "+ str(products.price))



        print (self.get_total_price())


    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!

        self.print_receipt()
        user_input ("Is this your order:") 

        if user_input.lower() == "yes":
            print ("Thank you for shopping with us")

        else:
            print ("Order has been canceled")






