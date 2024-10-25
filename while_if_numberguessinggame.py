print('GUESSING GAME')
print('Press 0 to Exit')

while True:
    num = int(input('Enter a Number: '))
    if num == 0:
           break
    elif(num ==50):
        print('Correct')
        break
    elif(num>10 and num<100):
        print('close')
    elif(num<10):
        print('too low')
    elif(num>100):
        print('too high')
    else:
        print('Not possible/ fix this program lol')
