import os

def menu_pizza_py():                                                                                                    # # Pizza Py (main menu)
  for item in menu_pizza_py_items:
    print('{}. {}'.format(item, menu_pizza_py_items[item]['name']))
  menu_selection = input('Welcome to Pizza.Py! How may we be of service? ')[:1]
  test_input = menu_pizza_py_items.get(menu_selection, "")
  if test_input:
    set_next_menu(menu_pizza_py_items[menu_selection]['action'])
  else:
    pizza_py_error()                                                                                                    # error handling (menu_pizza_py)

def menu_add_pizza():                                                                                                   # # Add a Pizza
  for item in menu_add_pizza_items:
    print('{}. {}'.format(item,menu_add_pizza_items[item]['name']))
  pizza_size_selection = input('What size pizza do you want? ')[:1]
  test_input = menu_add_pizza_items.get(pizza_size_selection, "")
  if test_input:
    print('Fetching you a {} pizza!'.format(menu_add_pizza_items[pizza_size_selection]['name']))
    # todo: add toppings, or select a specialty pizza
    # todo: set quantity
    # todo: add to cart, update subtotal
    set_next_menu('menu_pizza_py')
  else:
    pizza_py_error()                                                                                                    # error handling (menu_add_pizza)

def menu_del_pizza():                                                                                                   # # Remove a Pizza
  print("Failwhale. Why would you want to remove a pizza?!")
  input("This menu isn't ready yet. Press ENTER to continue...")
  # todo: find a pizza to remove
  set_next_menu('menu_pizza_py')

def menu_view_cart():                                                                                                   # # View your cart
  print("Huzzah! You've managed to order some pizza")
  input("This menu isn't ready yet. Press ENTER to continue...")
  #    Name        Size      Qty      ?    Cost
  # 1. Pizza 1     sm ( 8in)    2      3    $    16.00
  # 2. Jimbo       lg (12in)    1      1    $    11.00
  # edit pizza, add pizza, remove pizza, return to main
  # Pizza 1 - sm ( 8in) x2
  # add/remove toppings, change qty, remove
  set_next_menu('menu_pizza_py')

def menu_checkout():                                                                                                    # # Checkout and pay
  print("Time to pay the piper... er, pizza maker")
  input("This menu isn't ready yet. Press ENTER to continue...")
  # todo: view cart, pay now, return to main
  set_next_menu('menu_pizza_py')

def menu_exit():                                                                                                        # # Exit this program
  print("Fine! Be a quitter!")
  input("This menu isn't ready yet. Press ENTER to continue...")
  # todo: prompt to quit, save order for later
  exit()

def set_next_menu(next_menu_name):                                                                                      # # Set the next menu
  global next_menu                                                                                                      # D.R.Y.
  next_menu = next_menu_name                                                                                            # D.R.Y. ... XD

def pizza_py_clear():                                                                                                   # # Clear the screen
  os.system('cls' if os.name=='nt' else 'clear')

def pizza_py_status():                                                                                                  # # Status bar
  print('There are {} items in your cart. Estimated total is $ {:.2f}.\n'.format(len(cart), subtotal))

def pizza_py_error():                                                                                                   # # Error handling
  print("I pity the fool who can't order a pizza!")
  yn = input("Would you like to return to the previous menu? Type y or n")[:1]
  if yn == 'y':
    return
  else:
    set_next_menu('menu_exit')

# todo: curses, urwid, blessed for TUI
# # # # # # # #                                                                                                         # # Variables
cart = []                                                                                                               # cart
subtotal = float(0)                                                                                                     # subtotal
# these menus _could_ be tuples, like: menu_items = ( {'name': 'Add...', 'action': 'menu...'} )
# Tuples are faster and less prone to human error, but require extra code to avoid presenting '0' as an option.
# Dictionaries are slower, but can function like a switch-case by using the .get() method.
menu_pizza_py_items = {                                                                                                 # menu_pizza_py_items
  '1': {'name': 'Add a pizza',       'action': 'menu_add_pizza' },
  '2': {'name': 'Remove a pizza',    'action': 'menu_del_pizza' },
  '3': {'name': 'View your cart',    'action': 'menu_view_cart' },
  '4': {'name': 'Checkout and pay',  'action': 'menu_checkout' },
  '0': {'name': 'Exit this program', 'action': 'menu_exit' }
}
menu_add_pizza_items = {                                                                                                # menu_add_pizzas_items
  '1': {'cost':  5.00, 'diameter':  8, 'slices':  6, 'name': 'Small'},
  '2': {'cost':  7.50, 'diameter': 10, 'slices':  8, 'name': 'Medium'},
  '3': {'cost': 10.00, 'diameter': 12, 'slices':  8, 'name': 'Large'},
  '4': {'cost': 12.50, 'diameter': 14, 'slices': 10, 'name': 'X-Large'}
}
toppings = ('pepperoni', 'mushrooms', 'sausage', 'veggies', 'onions', 'broccoli')                                       # list of available toppings
toppings_cost = float(1.00)                                                                                             # fixed cost per topping
menu_specialty_items = {}

pizza_sample_object = {
  'name': 'Pizza 1',
  'size': 'Large' # for easy lookups, use 'type': '3' instead
  'toppings': [], # this will be filled in when toppings are selected
  'price': "",    # can be omitted. cost + len(toppings)*toppings_cost
  'quantity': 0   # user editable. if quantity = 0 then delete pizza from cart
}

next_menu = 'menu_pizza_py'                                                                                             # Set the first menu
# The while True: loop may need to be replaced, and set menu_exit() to return the value that kills the loop             # TODO
while True:                                                                                                             # loop forever, until exit()
  pizza_py_clear()                                                                                                      # clear buffer
  pizza_py_status()                                                                                                     # print status bar
  globals()[next_menu]()                                                                                                # load the requested menu
# https://medium.com/@samuel.fare/want-to-learn-any-programming-language-write-these-3-simple-apps-5af8cd119921         # inspired by
