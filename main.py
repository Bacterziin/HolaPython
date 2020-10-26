import metodosarchivos as mtd
# the open function take 2 parameters, filename and mode
# "r" Read defaul value, open a file for reading
# "a" Append Open a File for apeengind, create file if not exist
# "w" write opens a file for writing
# "x" create the specidied file
while (True):
    print("\n °° °° °° MENU °° °° °° °° \n ")
    print("""1.- Crear archivos \n2.- Agregar Contenido\n3.- Ver contenido \n4.- Eliminar archivos \n5.- Salir""")
    menu = input("ingresa una opcion: ")
    if menu == "1" or menu.lower() == "uno" or menu.lower() == "crear":
        filename = input("ingresa el nombre del nuevo archivo ")
        mtd.crearArchivo(filename)
    elif menu == "2" or menu.lower() == "dos" or menu.lower() == "agregar":
        filename = input("ingresa el nombre del archivo a adicionar texto: (si no existe lo creara) ")
        mtd.agregarTexto(filename)
    elif menu == "3" or menu.lower() == "tres" or menu.lower() == "leer":
        filename = input("ingresa el nombre del archivo que deseas leer: ")
        mtd.leerArchivo(filename)
    elif menu == "4" or menu.lower() == "cuatro" or menu.lower() == "eliminar":
        filename = input("ingresa el nombre del archivo que deseas E L I M I N A R: ")
        mtd.eliminarArchivo(filename)
    elif menu == "6" or menu.lower() == "seis" or menu.lower() == "crear varios":
        num = int(input("cuantos archivos deseas crear?: "))
        filename = input("ingresa el nombre del nuevo archivo ")
        for indice in range(1, num+1):
            mtd.crearArchivo(filename+str(indice))

