bdays = {'AC': 'Jan. 9th', 'Matt':'Jan. 7', 'Dad': 'Feb. 11th', 'Nick': 'Mar. 14'}
while True:
    print('Enter a name:  (blank to quit)')
    name = input()
    if name == '':
        break

    if name in bdays:
        print(bdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday informaton for ' + name)
        print('What is their birthday?')
        new_bday = input()
        bdays[name] = new_bday
        print('Birthday database updated.')
        
         
