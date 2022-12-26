import os
from ModuloCertificados import AuxFunc
from PyPDF2 import PdfReader
from progress.bar import ChargingBar

def Renombrar():
    # devuelve directorio del programa
    saved_path = os.getcwd()

    # Crea lista de nombres del directorio
    file_list = AuxFunc.nameList(saved_path + "/Certificados")
    # lista de documentos
    docList = []
    # lista de Repetidos
    Repetidos = []

    if len(file_list) != 0:
        bar1 = ChargingBar('Renombrando...', max=(len(file_list)+1))
        bar1.next()

        for name in file_list:
            text = ''
            direccion = saved_path + "/Certificados/" + name
            # with pdfplumber.open(direccion) as temp:
            #     page = temp.pages[0]
            #     text = page.extract_text()
            reader = PdfReader(direccion)
            page = reader.pages[0]
            text = page.extract_text()

            dni = AuxFunc.dni_extract(text)
            docList.append(dni)

            newName = AuxFunc.newName(name, dni)

            file = saved_path + "/Certificados/" + name

            saveNew = saved_path + "/Certificados/" + newName

            os.rename(file, saveNew)
            
            bar1.next()

        # --------------Revisar Repetidos----------------
        print("\n")
        Repetidos = AuxFunc.listDups(docList)

        if len(Repetidos) != 0:
            print("Generando lista de repetidos...")
            print("Los documentos repetidos son: ")
            print(Repetidos)
            print("En total hay " + str(len(Repetidos)) + " duplicados.")

        else:
            print("No se encontraron elementos repetidos.")

    else:
        print("No hay certificados cargados")

    print("\n Tarea completada (Buscar en carpeta 'Certificados') \n")
