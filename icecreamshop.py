import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Creating a queue of dictionaries, per customer
# The queue will sort itself by the total "cost" of their order.
class CustomerQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def add_customer(self, name, item, cost):
        customer_dict = {"name": name,
                         "item": item,
                         "cost": cost}
        self.enqueue(customer_dict)
        self.items.sort(key=lambda x: x["cost"], reverse=True)

    def next_customer(self):
        if self.is_empty():
            return None
        return self.dequeue()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

    

# Shop is a subclass of the Queue
class IceCreamShop(CustomerQueue):
    def __init__(self, worker):
        self.worker = worker
        super().__init__()
        self.flavors = {
            "Birthday Cake": "%.2f$" % random.uniform(1.00, 12.00),
            "Brownie": "%.2f$" % random.uniform(1.00, 12.00),
            "Cheesecake": "%.2f$" % random.uniform(1.00, 12.00),
            "Chocolate": "%.2f$" % random.uniform(1.00, 12.00),
            "Chocolate Chip": "%.2f$" % random.uniform(1.00, 12.00),
            "Chunky Monkey": "%.2f$" % random.uniform(1.00, 12.00),
            "Coffee": "%.2f$" % random.uniform(1.00, 12.00),
            "Coconut": "%.2f$" % random.uniform(1.00, 12.00),
            "Cookie Dough": "%.2f$" % random.uniform(1.00, 12.00),
            "Fudge": "%.2f$" % random.uniform(1.00, 12.00),
            "Green Tea": "%.2f$" % random.uniform(1.00, 12.00),
            "Pistachio": "%.2f$" % random.uniform(1.00, 12.00),
            "Snickerdoodle": "%.2f$" % random.uniform(1.00, 12.00),
            "Strawberry": "%.2f$" % random.uniform(1.00, 12.00),
            "Vanilla": "%.2f$" % random.uniform(1.00, 12.00),
            "Waffle": "%.2f$" % random.uniform(1.00, 12.00),
        }
        self.flavors = dict(sorted(self.flavors.items()))
        
        # Names to use for the "customers" dictionaries
        self.random_names = [
            "Agent S",
            "Agnes",
            "Beau",
            "Bianca",
            "Boots",
            "Bunnie",
            "Celia",
            "Chevre",
            "Cole",
            "Daisy",
            "Filbert",
            "Freckles",
            "Goldie",
            "Hopper",
            "Lolly",
            "Marina",
            "Mitzi",
            "Olaf",
            "Peaches",
            "Pekoe",
            "Poppy",
            "Rosie",
            "Ruby",
            "Stella",
            "Zell"
        ]
        
        
        
    # Giving the user the option to start and stop
    def employee_greet(self, worker):
        print('''
        ____________________________________
       / \                                  \
      /   \                                  \
     /     \                                  \
    /   |\  \                                  \
   /    | \  \                                  \
  /     |  \  \                                  \
 /______|___\__\__________________________________\
 \___________\__\__\_______________________________|
 |˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚˚ʚ♡ɞ˚|
 |          WELCOME TO THE ICE CREAM SHOP!          |
 |        ♡♡♡        ♡ ♡  (*ᴗ͈ˬᴗ͈)ꕤ*.ﾟ   ♡    ♡♡♡     |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |                                                  |
 |__________________________________________________|
        ''')
        time.sleep(0.5)
        print(f"Hello {worker}, Welcome to your first day on the job!")
        time.sleep(0.5)
        print("Here are the flavors we are offering today . . . ♡ ")
        for flavor, cost in self.flavors.items():
            print(f"{flavor}: {cost}")
            time.sleep(0.5)
        confirm_start = input("Are you ready to begin? Type Y to continue, or N to exit.").lower()
        if confirm_start.lower() == "y" or "yes":
            time.sleep(0.5)
            print("Great, let's get started!")
        elif confirm_start.lower() == "n" or "no":
            time.sleep(0.5)
            print("Thank you, have a nice day!")
        else:
            time.sleep(0.5)
            print("Invalid input, please try again . . . ")
            
        
        
        # Generating customers
    def generate_customers(self, worker):
        time.sleep(0.5)
        num_customers = int(input(f"{worker}, how many customers can we handle today?: "))
        try:
            if num_customers > 50:
                time.sleep(0.5)
                print("Sorry, we cannot handle more than 50 customers at a time.")
                return
            elif num_customers < 3:
                time.sleep(0.5)
                print("We need more customers than that!")
                return
            else:
                time.sleep(0.5)
                print("Great! Let's do this!")
                print("STARTING ORDERS . . . ")
                print("Please wait and do not exit.")
                for i in range(num_customers):
                    name = random.choice(self.random_names)
                    item = random.choice(list(self.flavors.keys()))
                    cost = self.flavors[item]
                    customer = {
                        "name": name,
                        "item": item,
                        "cost": cost
                    }
                    self.add_customer(name, item, cost)
                    time.sleep(0.5)
        except ValueError:
            print("Invalid entry, please try again")
            return
            
            
            
            
    # Printing the queue of all customers
    def serve_customers(self, worker):
        print(f"\nYou have {self.size()} orders.")
        print("(✦✦✦✦✦✦✦✦ PRIORITY ORDERS ✦✦✦✦✦✦✦✦)")
        orders = self.items.copy()
        for customer in orders:
            customer = self.next_customer()
            print(f"{customer['name']} ordered a scoop of {customer['item']} flavor.")
            time.sleep(0.5)
            print("✦ %s filled the order of %s for %s! %d orders remaining. ✦" % (worker, customer['item'], customer['name'], self.size()))
            time.sleep(0.5)
        print("\n\nYou completed all orders!")
        time.sleep(0.5)
        print("Great job!")
        print("Goodbye!")
        time.sleep(1)
       
        
    
    

       
     
    
store = IceCreamShop("Mesunie")
store.employee_greet("Mesunie")
store.generate_customers("Mesunie")
store.serve_customers("Mesunie")






             
                



        


