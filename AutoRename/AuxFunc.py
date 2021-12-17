import os

#Crea una lista con los nombres de todos los archivos de la dirección pasada como parametro
def nameList(directorio):
    file_list = os.listdir(directorio)
    return file_list

#Extrae el DNI de el string de certificados
def dni_extract(file_string):
    DNI = [int(temp) for temp in file_string.split() if temp.isdigit()]
    DNI = DNI[0]
    return DNI

#Crear nombre nuevo
def newName(name, DNI):
    # Eliminar #
    name = name.split('#')[0] + name.split('#')[1]
    # Nombre nuevo
    #print(name)
    newName = str(DNI) + '_' + name

    return newName

#Devuelve los elementos duplicados de una lista
def listDups(lDocs):
    aux = []
    repetidos = []
    for dni in lDocs:
        if dni not in aux:
            aux.append(dni)
        else:
            if dni not in repetidos:
                repetidos.append(dni)

    return repetidos

#Eliminar Repetidos
def eliminaRepetidos(Repetidos):
    # devuelve directorio del programa
    saved_path = os.getcwd()

    # Crea lista de nombres del directorio
    file_list = nameList(saved_path + "/CorrectName")

    mover = []

    for dni in Repetidos:
        for file in file_list:
            doc = file.split("_")[0]

            if doc == dni:
                mover.append(file)

    flag = ""
    for name in mover:
        doc = name.split("_")[0]
        if flag == doc:
            file = saved_path + "/CorrectName/" + name
            saveNew = saved_path + "/Duplicados/" + doc
            os.rename(file, saveNew)

        else:
            flag = doc