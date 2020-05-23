import re
expresion = r'([0-9])'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
a=1
if busqueda:
    print busqueda.group()
    while a<=10:
        print int(prueba[0])*a
        a+=1
else:
    print "qr"
