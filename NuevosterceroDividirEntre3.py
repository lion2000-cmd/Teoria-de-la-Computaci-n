import re
expresion = r'([a-z]+||[0-9]+)(\@)([a-z]+)(\.)([a-z]+)'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print "qA"
    print prueba 
else:
    print "qr"
