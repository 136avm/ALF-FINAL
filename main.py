import silabeador
import entonacion
import diccionario

D = diccionario.leerDiccionario()

if __name__ == "__main__":
    print("")
    print("=========================================================")
    print("PROYECTO FINAL PRÁCTICAS - AUTÓMATAS Y LENGUAJES FORMALES")
    print("=========================================================")
    print("")
    while 1==1:
        print("OPCIONES:")
        print("1. Silabear una palabra.")
        print("2. Clasificar una palabra según su entonación.")
        print("3. Salir.")
        print("")
        option = input("Introduzca una opción (1-3): ")
        if option=="1":
            palabra = input("Introduce una palabra para silabear: ")
            res = diccionario.comprobarAst(palabra, D)
            if res == []:
                silabas = silabeador.silabear(palabra)
                diccionario.insertarSilabas(palabra, silabas, D)
            else:
                if res[0] != []:
                    silabas = res[0]
                else:
                    silabas = silabeador.silabear(palabra)
                    diccionario.insertarSilabas(palabra, silabas, D)
            print("Tu palabra dividida en sílabas es: "+str(silabas))
        elif option=="2":
            palabra = input("Introduce una palabra para saber su entonación: ")
            res = diccionario.comprobarAst(palabra, D)
            if res == []:
                ent = entonacion.entonacion(palabra)
                diccionario.insertarEntonacion(palabra, ent, D)
            else:
                if res[1] != '':
                    ent = res[1]
                else:
                    ent = entonacion.entonacion(palabra)
                    diccionario.insertarEntonacion(palabra, ent, D)
            print("Tu palabra es " + ent + ".")
        elif option=="3":
            diccionario.escribirDiccionario(D)
            break
        else:
            print("Introduzca una opción válida.")
        print("")
    print("¡Hasta la próxima!")