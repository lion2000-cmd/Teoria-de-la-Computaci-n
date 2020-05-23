import re
expresion = r'(1)(0)(1)'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print "qr"
