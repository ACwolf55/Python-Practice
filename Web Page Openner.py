##web page opener##

import webbrowser

print('WEB PAGE OPENNER \n')

print(' 1 = PokeCommunity \n 2 = Amazon \n 3 = Reddit \n 4 = Gmail')

x = int(input('\n Choose webpage to open: '))

if x == 1:
          webbrowser.open('https://www.pokecommunity.com/')

elif x == 2:
           webbrowser.open('https://www.amazon.com/')

elif x == 3:
          webbrowser.open('https://www.reddit.com/')

elif x == 4:
          webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

else:
    print('Invalid Entry \n\n\n\n\n\n')

