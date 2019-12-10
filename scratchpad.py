# # Tuple-based Text Menu                                                                                               # # # #
tuple_items = (                                                                                                         # Create the Tuple
  {'keyword': 'add', 'desc': 'First human-readable option',  'action': 'function_that_adds'},                           # Option 1, based on tuple order
  {'keyword': 'rm',  'desc': 'Second human-readable option', 'action': 'function_that_rms'}                             # Option 2, based on tuple order
)

# Display the menu                                                                                                      # #
for item in range(0,len(tuple_items)):
  print('{}. {} (or type {})'.format(item+1,tuple_items[item]['desc'],tuple_items[item]['keyword']))

my_keyword = input("Please select an option: ")                                                                         # User input
next_action = ''                                                                                                        # What's next?
for item in range(0,len(tuple_items)):                                                                                  # Loop it!
  if my_keyword == tuple_items[item]['keyword'] or my_keyword == str(item+1):                                           # Does it match?
    print('Success! We found a match. Your next function is {}'.format(tuple_items[item]['action']))                    # yes it do!
    next_action = tuple_items[item]['action']                                                                           # action jackson

# Do we know what to do?                                                                                                # #
if next_action:                                                                                                         # take action!
  print('we should be running {}() right now...'.format(next_action))                                                   #
  #globals()[next_action]()                                                                                             #
else:                                                                                                                   # fix problems!
  print('You done messed up A-A-Ron!')                                                                                  #
