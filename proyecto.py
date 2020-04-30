while True:
    p=raw_input("ingresa la operacion\n")
    a=p.lower()

    if a=="":
        break
    a+=";"
    estado="q0"
    for entrada in a:
        if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
            for entrada in p:
                if estado=="q0":
                    if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                        estado="q1"
                        pal1=entrada
                    if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="10" or entrada=="0"or entrada==";";:
                        print "no ingresaste letra"
                        estado = "qr"
                    else:
                        print entrada
            break

        elif entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="10" or entrada=="0":
            print entrada
            break

        else:
           print "error"

