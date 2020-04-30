numero = raw_input("ingresa un numero?")
numero=int(numero)
i=1
for i in range(1,11):
    tabla =  numero*i
    print "%s * %s = %s"%(i,numero,tabla)
    
