import re
expresion = r'([0-9]+)(\+||\-||\*||\/)([0-9])'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print "qA"
    print busqueda.group()
    
else:
    print "qr"
