def get_orders(names, egg_order):
    """
    Collects order information - name, number of eggs – in a loop. Store in 2 lists.
    Call read_int function to ensure you have a valid input
    """

    print ("Collecting Orders")
    ?
    ?
    ?

def show_orders(names, egg_order):
    """
    calculates price for each egg order, and displays order information - name, number of eggs, price
    """
    PRICE_PER_DOZEN = 6.5
    print("Showing orders")
    ?
    ?
    ?


def show_report(egg_order):
    """
    displays summary - total eggs, number of dozens to be ordered, average eggs per customer.
    Print "No orders" if no orders received otherwise print "Summary , Total eggs and Dozens required (call get_dozens function)
    as well as Average"
    """

     ?
     ?
     ?

def get_dozens (num_eggs):
    """
    returns whole number of dozens required to meet required number of eggs
    """
   
     ?
     ?
     ?

def read_pos_int(prompt):

      ?
      ?
      ?
      
#main routine

names = []
egg_order = []
get_orders(names, egg_order)
show_orders(names, egg_order)
show_report(egg_order)
