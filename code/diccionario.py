import csv
import silabeador
import ast

cambio = "[,'"

def comprobarAst(palabra, D):
    if palabra in D:
        x = D.get(palabra)
        if len(x) == 2:
            res = [x[0], x[1]]
            return res
        else:
            x = ast.literal_eval(str(x))
            res = [x[0], x[1]]
            return res
    else:
        return []

#Devuelve el contenido del diccionario, y si no existe devuelve un array vacío
def comprobar(palabra, D):
    comprobarAst(palabra, D)
    #Comprobamos que la palabra está en D
    if palabra in D:
        x = D.get(palabra)
        #Comprueba que la palabra no es leída del CSV sino introducida en esta ejecución
        if len(x) == 2:
            res = [x[0], x[1]]
        #Palabra leída de fichero
        else:
            #Conseguir valor de la palabra
            pal = ''
            i = -3
            while x[i] != "'":
                pal = x[i] + pal
                i -= 1
            #Conseguir valor de las sílabas
            sils = ''
            i = 0
            while x[i] != ']':
                sils = sils + x[i]
                i += 1
            for c in cambio:
                sils = sils.replace(c, '')
            sils = sils.replace(' ', '')
            if sils != '':
                sils = silabeador.silabear(sils)
            else:
                sils = []
            #Actualizar valor del diccionario
            res = [sils, pal]
        #Devolver valor del diccionario en caso de existir la palabra en él
        return res
    else:
        return []


def leerDiccionario():
    try:
        with open("dict.csv") as f:
            reader = csv.reader(f)
            D = dict(reader)
    except:
        D = {}
    return D


def insertarSilabas(palabra, silabas, D):
    if palabra in D:
        x = D.get(palabra)
        if len(x) == 2:
            if x[1]=='':
                D[palabra] = [silabas,'']
            else:
                D[palabra] = [silabas,x[1]]
        else:
            """
            pal = ''
            i=-3
            while x[i] != "'":
                pal = x[i]+pal
                i-=1
            """
            pal = comprobar(palabra, D)
            pal = pal[1]
            if pal == '':
                D[palabra] = [silabas, '']
            else:
                D[palabra] = [silabas, pal]
    else:
        D[palabra] = [silabas, '']


def insertarEntonacion(palabra, entonacion, D):
    if palabra in D:
        x = D.get(palabra)
        if len(x) == 2:
            if x[0]==[]:
                D[palabra] = [[],entonacion]
            else:
                D[palabra] = [x[0],entonacion]
        else:
            """
            sils = ''
            i = 0
            while x[i] != ']':
                sils = sils+x[i]
                i+=1
            for c in cambio:
                sils = sils.replace(c, '')
            sils = sils.replace(' ', '')
            sils = silabeador.silabear(sils)
            """
            sils = comprobar(palabra, D)
            sils = sils[0]
            if sils == []:
                D[palabra] = [[], entonacion]
            else:
                D[palabra] = [sils, entonacion]

    else:
        D[palabra] = [[], entonacion]


def escribirDiccionario(D):
    with open("dict.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for k, v in D.items():
            writer.writerow([k, v])