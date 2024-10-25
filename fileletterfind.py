f = open('inputFile.txt','r')
for line in f:
    linesplit = line.split()
    if linesplit[2] == 'P':
        print(line)
    
    
f.close()
