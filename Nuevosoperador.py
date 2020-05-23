import re
expresion = r'([0-9]+)(\+||\-||\*||\/)([0-9])'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print "qA"
    print busqueda.group()
    if prueba[1]=="+":
        print int(prueba[0])+ int(prueba[2])
    elif prueba[1]=="-":
        print int(prueba[0])- int(prueba[2])
    elif prueba[1]=="*":
        print int(prueba[0])* int(prueba[2])
    elif prueba[1]=="/":
        print int(prueba[0])/ int(prueba[2])
    else:
        print "qR"
    
else:
    print "qr"
