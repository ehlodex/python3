import os

cart = []
subtotal = float(0)
sales_tax = float(.06)
status_bar = 'Welcome to Pizza Py!'
pizzas = {
  'cheese':    5.00,
  'pepperoni': 6.00,
  'broccoli': 10.00
}

def pizza_py_clear():                                                                                                   # # Clear the screen
  print('\n' * 80) # this is a hack to clear the output in PyCharm.                                                     # Please delete this line
  os.system('cls' if os.name=='nt' else 'clear')                                                                        # 'cls' for Win, 'clear' for everyone else

def pizza_py_status():                                                                                                  # # Status bar
  print('There are {} items in your cart. Estimated total (with {:.1f}% tax) is: $ {:6>.2f}'.format(len(cart),sales_tax*100,subtotal*(1+sales_tax)))
  for pizza in pizzas:                                                                                                  # iterate through the pizza types
    pizza_qty = cart.count(pizza)                                                                                       # count number of type in cart
    pizza_subtotal = pizza_qty*pizzas[pizza]                                                                            # qty * cost
    print ('- {:<10} : {:>2} at $ {:>5.2f} each (${:7.2f})'.format(pizza,pizza_qty,pizzas[pizza],pizza_subtotal))       # Print cart status by pizza type
  print ('---- '*4 + '\n\n{}\n\n'.format(status_bar) + '---- '*4)                                                       # Print status_bar

while True:                                                                                                             # # Execute forever (until stopped)
  pizza_py_clear()                                                                                                      # Clear output
  pizza_py_status()                                                                                                     # Print status
  for pizza in pizzas:                                                                                                  # iterate through the pizza types
    print('{:<12} $ {:>5.2f}'.format(pizza, pizzas[pizza]))                                                             # Print the pizza types and prices
  my_selection = input('Please select a pizza: ')                                                                       # Order up!
  if pizzas.get(my_selection, False):                                                                                   # Did you make a good choice?
    cart.append(my_selection)                                                                                           # Add pizza type to cart
    subtotal = subtotal + pizzas[my_selection]                                                                          # update the subtotal
    status_bar = 'Successfully added a {} pizza!'.format(my_selection)                                                  # Set status_bar (success)
  else:                                                                                                                 # Can't type?
    status_bar = 'You done messed up, A-A-Ron! \'{}\' is not a pizza!'.format(my_selection)                             # Set status_bar (error)
# https://medium.com/@samuel.fare/want-to-learn-any-programming-language-write-these-3-simple-apps-5af8cd119921         # # inspired by
