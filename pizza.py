import os

cart = []
subtotal = float(0)
sales_tax = float(.06)
status_bar = 'Welcome to Pizza Py! Please select a pizza or type \'exit\'.'
pizzas = {
    'cheese':    5.00,
    'pepperoni': 6.00,
    'broccoli': 10.00
}

def pizza_py_clear():
    print('\n' * 80) # this is a hack to clear the output in PyCharm
    # For Windows, issue 'cls' for all others, issue 'clear'
    os.system('cls' if os.name=='nt' else 'clear')

def pizza_py_status():
    print('There are {} items in your cart. Estimated total (with {:.1f}% tax)'
          ' is: $ {:6>.2f}'
          .format(len(cart), sales_tax*100, subtotal*(1+sales_tax)))
    for pizza in pizzas:
        pizza_qty = cart.count(pizza)
        pizza_subtotal = pizza_qty*pizzas[pizza]
        print ('- {:<10} : {:>2} at $ {:>5.2f} each (${:7.2f})'
               .format(pizza, pizza_qty, pizzas[pizza], pizza_subtotal))
    print ('---- '*4 + '\n\n{}\n\n'.format(status_bar) + '---- '*4)

while True:
    pizza_py_clear()
    pizza_py_status()
    for pizza in pizzas:
        print('{:<12} $ {:>5.2f}'.format(pizza, pizzas[pizza]))
    my_selection = input('Please select a pizza: ')
    if my_selection == 'exit':
        exit()
    if pizzas.get(my_selection, False):
        cart.append(my_selection)
        subtotal = subtotal + pizzas[my_selection]
        status_bar = 'Successfully added a {} pizza!'.format(my_selection)
    else:
        status_bar = 'You done messed up, A-A-Ron! \'{}\' is not a pizza!'\
                     .format(my_selection)
# https://medium.com/@samuel.fare/want-to-learn-any-programming-language-write-these-3-simple-apps-5af8cd119921
