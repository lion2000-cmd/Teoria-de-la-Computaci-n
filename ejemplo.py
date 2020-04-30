n = raw_input("numero: ")

try:
    n = int(n)
    n = n + 1
    print n
    
except:
    print "%s no es un numero" %(n)
