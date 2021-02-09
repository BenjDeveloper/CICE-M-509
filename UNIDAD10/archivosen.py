
import re
myfile=open("./cotizacion.csv","r")

myfile=myfile.read()
myfile=re.split(";|\n",myfile)
# print(re.split(";|\n",myfile))
# print(myfile)
empresa=dict()
for line in range(6,len(myfile)-1,6):
    # print(myfile[line:line+6])
    miempresa=myfile[line:line+6]
    empresa[miempresa[0]]={"Final":float(miempresa[1].replace('.', '').replace(',','.')),"Máximo":float(miempresa[2].replace('.', '').replace(',','.')),"Mínimo":float(miempresa[3].replace('.', '').replace(',','.')),"Volumen":float(miempresa[4].replace('.', '').replace(',','.')),"Efectivo":float(miempresa[5].replace('.', '').replace(',','.'))}
# print(empresa)
def imprimir(diccionario):
    for key, value in diccionario.items():
        print(key,value)

# imprimir(empresa)
def guardar(dicc):
    output=open("./salida.csv","w")
    # output.writelines(";".join(["Nombre","Final","Máximo","Mínimo","Volumen","Efectivo"]))
    maximo=[0,0,0,0,0]
    minimo=[0,0,0,0,0]
    media=[0,0,0,0,0]
    contitems=0
    for value in dicc.values():
        # print(value)
        # print(list(value.values()))
        for x,y,index in zip(list(value.values()),maximo,range(0,6)):
            # print(x,y,index)
            # print(type(x),type(y),type(index))
            maximo[index]=max(x,y)
        if contitems==0:
            minimo=list(value.values())
        else:
            for x,y,index in zip(list(value.values()),minimo,range(0,6)):
                minimo[index]=min(x,y)
        for x,y,index in zip(list(value.values()),media,range(0,6)):
            media[index]=x+y
        contitems+=1
    media=[num/contitems for num in media]
    print(maximo)
    print(minimo)
    print(media)
    output.writelines("Máximo;"+";".join(str(v) for v in maximo))
    output.writelines("Mínimo;"+";".join(str(v) for v in minimo))
    output.writelines("Media;"+";".join(str(v) for v in media))

guardar(empresa)
