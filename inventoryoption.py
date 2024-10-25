inventory = {} #Empty inventory
                #{key:value} ex.{'Sword':2, 'Gold',500}

print('''
      Inventory Options
      -----------------
      1. Add Item
      2. Remove Item
      3. View inventory
      0. Exit
''')

option = int(input('Choose Option: '))
while option !=0:
    if option ==1:
        item = input('Enter Item: ')
        qnty = int(input('Enter quantity: '))
        inventory[item]=qnty
        
    elif option ==2:
        item = input('Choose item from inventory: ')
        del (inventory[item])
        
    elif option ==3:
        for item in inventory:
            print(item,':',inventory[item])
            
    elif option !=0:
        print('-Enter valid number-')
        
    option = int(input('\n\nChoose an option: '))

else:
     print('Inventory Closed')
