import math
while True:
    p= raw_input("ingresa la operacion y termina con un ;\n")
    if p=="":
        break
    p += ";"
    estado="q0"

    simbolo = None
    sim = None
    n1 = None
    n2 = None
    np = 0
    nI1="0"
    nI2="0"
    for entrada in p:
        if estado=="q0":
            if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9": 
                estado="q1"
                n1=entrada
            if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                estado="q2"
                n1=entrada
            if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                estado="qR"            
                raiz=entrada
        elif estado=="q1":
            if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                estado="q1"
                n1+=entrada
            if entrada==" ":
                estado="q3"
            if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z" or entrada==";":
                print "Caracter inesperado"
                estado="qR"
        elif estado=="q2":
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="q2"
                 n1+=entrada
             if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                 estado="qr"
                 n2=None
                 n1=None
                 simbolo=None
             if entrada==" ":
                 estado="q3"
             if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada==";":
                 estado="qr"
                 entrada=None
                 exit
        elif estado=="q3":
             if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/" or entrada=="#" or entrada=="^":
                 estado="q4"
                 simbolo=entrada
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="q5"
                 simbolo=entrada
             if entrada==";" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                 estado="qr"
                 entrada=None
        elif estado=="q4":
             if  entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="qr"
                 simbolo=None
                 break
             if entrada=="+" or entrada=="*" or entrada=="/" or entrada=="-" or entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                 estado="qr"
                 simbol=None
                 n2="0"
                 break
             if entrada==" ":
                 estado="q6"
        elif estado=="q5":
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="q5"
                 simbolo+=entrada
             if entrada==" ":
                 estado="q6"
             if entrada=="+" or entrada=="*" or entrada=="-" or entrada=="/" or entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada==";":
                 estado="qr"
                 simbolo=None
                 exit
        elif estado=="q6":
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="q8"
                 n2=entrada
             if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                 estado="q7"
                 n2=entrada
             if entrada=="+" or entrada=="*" or entrada=="-" or entrada=="/" or entrada==";": 
                 estado="qr"
                 entrada=None
                 n2="0"
        elif estado=="q7":
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="qr"
             if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                 estado="q7"
                 n2+=entrada
             if entrada=="+" or entrada=="*" or entrada=="-" or entrada=="/": 
                 estado="qr"
                 entrada=None
                 n2="0"
             if entrada==";": 
                 estado="qa"  
            
        elif estado=="q8":
             if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or entrada=="j" or entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
                 estado="q8"
                 n2+=entrada
             if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
                 estado="qr"
                 entrada=None
             if entrada=="+" or entrada=="*" or entrada=="-" or entrada=="/": 
                 estado="qr"
                 n2="None"
             if entrada==";": 
                 estado="qa"                
                 
        elif estado=="qR" or estado=="qA":
            break
            exit     
        

    print n1
    print simbolo
    print n2
    try:
        nI1=int(n1)    
    except:
        print estado
        if n1=="dos":
            nn1="2"
            nI1=int(nn1)
        elif n1=="uno":
            nn1="1"
            nI1=int(nn1)
        elif n1=="tres":
            nn1="3"
            nI1=int(nn1)
        elif n1=="cuatro":
            nn1="4"
            nI1=int(nn1)
        elif n1=="cinco":
            nn1="5"
            nI1=int(nn1)
        elif n1=="seis":
            nn1="6"
            nI1=int(nn1)
        elif n1=="siete":
            nn1="7"
            nI1=int(nn1)
        elif n1=="ocho":
            nn1="8"
            nI1=int(nn1)
        elif n1=="nueve":
            nn1="9"
            nI1=int(nn1)
        elif n1=="cero" :
            nn1="0"
            nI1=int(nn1)
        elif n1=="sen" or n1=="sin" or n1=="seno":
            nI1="s"
        elif n1=="cos" or n1=="coseno":
            nI1="c"
        elif n1=="tan" or n1=="tangente":
            nI1="t"
        else:
            print " numero equivocado :("
            n1=None
            n2=None
            simbolo=None
            exit
    try:
       nI2=int(n2)
    except:   
        if n2=="dos":
            nn2="2"
            nI2=int(nn2)
        elif n2=="uno":
            nn2="1"
            nI2=int(nn2)
        elif n2=="tres":
            nn2="3"
            nI2=int(nn2)
        elif n2=="cuatro":
            nn2="4"
            nI2=int(nn2)
        elif n2=="cinco":
            nn2="5"
            nI2=int(nn2)
        elif n2=="seis":
            nn2="6"
            nI2=int(nn2)
        elif n2=="siete":
            nn2="7"
            nI2=int(nn2)
        elif n2=="ocho":
            nn2="8"
            nI2=int(nn2)
        elif n2=="nueve":
            nn2="9"
            nI2=int(nn2)
        elif n2=="cero":
            nn2="0"
            nI2=int(nn2)
        else:
            print " numero equivocado :("
            n1=None
            n2=None
            simbolo=None
            exit
            
    if simbolo=="mas" or simbolo=="+":
        sim="+"
    elif simbolo=="menos" or simbolo=="-":
        sim="-"
    elif simbolo=="por" or simbolo=="*":
        sim="*"
    elif simbolo=="entre" or simbolo=="/":
        sim="/"
    elif simbolo=="^" or simbolo=="potencia" or simbolo=="pot":
        sim="p"
    elif simbolo=="de":
        sim="de"
    elif simbolo=="#" or simbolo=="raiz":
        sim="r"
    else:
        print " simbolo equivocado :("
        exit    

    if sim=="+":
        if estado=="qa" and type(nI1)==int and type(nI2) == int:
            print nI1+nI2
        else:
            exit
    elif sim=="-":
        if estado=="qa" and type(nI1)==int and type(nI2) == int:
            print nI1-nI2
        else:
            exit
    elif sim=="*":
        if estado=="qa" and type(nI1)==int and type(nI2) == int:
            print nI1*nI2
        else:
            exit
    elif sim=="/":
        if estado=="qa" and type(nI1)==int and type(nI2) == int:
            print nI1/nI2
        else:
            exit
    elif nI1=="s" and sim=="de" and estado=="qa" and type(nI2) == int:
        if estado=="qa":
            ss=float(math.sin(nI2))
            print ss
        else:
            exit
    elif nI1=="c" and sim=="de" and type(nI2) == int:
        if estado=="qa":
            ss=float(math.cos(nI2))
            print ss
        else:
            exit
    elif nI1=="t" and sim=="de" and type(nI2) == int:
        if estado=="qa":
            ss=float(math.tan(nI2))
            print ss
        else:
            exit
    elif sim=="p" and estado=="qa" and type(nI1) ==int and type(nI2)==int:
        if estado=="qa":
            pot = pow(nI1, nI2)
            print pot
        else:
            exit
    elif sim=="r" and estado=="qa" and type(nI1) ==int and type(nI2)==int:
        if estado=="qa":
            rais=(nI1**(1.0/nI2))
            print rais
    
        
            
    
    
    
    
