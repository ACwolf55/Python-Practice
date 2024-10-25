f = open('inputFile.txt','r')
passFile = open('PassFile.txt','w')
for line in f:
    linesplit = line.split()
    if linesplit[2] == 'P':
        passFile.write(line)
        
    
f.close()
passFile.close()
