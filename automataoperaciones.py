p= raw_input("ingresa la operacion \n") + ";"

estado="q0"
for entrada in p:
    if estado=="q0":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
            estado="q1"
        if entrada==";":
            estado="qR"
                  
    elif estado=="q1":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
            estado="q1"
        if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
            estado="q2"
        if entrada==";":
            estado="qR"    
    elif estado=="q2":
         if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
             estado="q3"
         if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/" or entrada==";":
            estado="qR"    
    elif estado=="q3":
         if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
             estado="q3"
         if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
             estado="q2"
         if entrada==";":
             estado="qA"        
             
    elif estado=="qR" or estado=="qA":
        break
print estado             
  





















 
