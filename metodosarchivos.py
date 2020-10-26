import io
from os import remove
def crearArchivo(nombre):
    try:
        if ".txt" in nombre:
           archivo = open(nombre)
           archivo.close()

        else:
            archivo = open(f"{nombre}.txt","x")
            archivo.close()
        print(" ARCHIVO CREADO CORRECTAMENTE")
    except: print("EL ARCHIVO YA EXISTE PUÑETON")
def agregarTexto(nombre):

    if ".txt" in nombre:
       archivo = open(nombre,"a")
       texto = input(f"escribe el texto que deseas añadir al archivo {nombre}: ")
       texto = texto + "\n"
       archivo.write(texto)
       archivo.close()
    else:
        archivo = open(f"{nombre}.txt","a")
        texto = input(f"escribe el texto que deseas añadir al archivo {nombre}.txt: ")
        archivo.write(texto)
        archivo.close()
def leerArchivo(nombre):
    numlineas = 1
    if ".txt" in nombre:
        archivo = open(nombre,"r")
        print("el contenido es: \n ----------------------------")
        for linea in archivo:
            print(f"{numlineas}.- {linea}",end = "")
            numlineas +=1
    else:
        archivo = open(f"{nombre}.txt","r")
        print("el contenido es: \n ----------------------------")
        for linea in archivo:
            print(f"{numlineas}.- {linea}", end = "")
            numlineas +=1
    print("\n fin del contenido  ----------------------------\n \n")
def eliminarArchivo(nombre):
    try:
        if ".txt" in nombre:
            remove(nombre)
        else:
            remove(f"{nombre}.txt")
    except:
        print("El sistema no encontro el archivo o estas todo puñetas  y no estas borrando un TXT\n ")