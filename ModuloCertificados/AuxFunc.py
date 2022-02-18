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
    if len(name.split('#')) > 1:
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