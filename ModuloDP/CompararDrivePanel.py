import pandas as pd

#---- Separar en listas de aprobados y reprobados de panel ----
def crearListasAR(listaPanel, lAprobados, lReprobados):
    for participante in listaPanel:
        dni = participante[0]
        condicion = participante[1]
        if condicion == "APROBADO":
            lAprobados.append(dni)
        elif condicion == "REPROBADO":
            lReprobados.append(dni)


#------ Devuelve los elementos que no estan en ambas listas -------
def noEncontrados(lista1, lista2):
    listaNoEncontrados = []

    for dni in lista1:
        flag = False
        for elem in lista2:
            if elem == dni:
                flag = True
        if flag == False:
            listaNoEncontrados.append(dni)

    return listaNoEncontrados

#------- Comprobar que las listas son iguales ------
def listasIguales(lista1, lista2):
    flag = True
    for elem1 in lista1:
        flag2 = False
        for elem2 in lista2:
            if elem2 == elem1:
                flag2 = True
        if flag2 == False:
            return False

    return  True

#======================================================================================================================
#                                                           RUN
#======================================================================================================================
def ValidarErroresDrivePanel():
    print("Comprobando listas de Drive y Panel...")
    # Extrae los documentos y condiciones finales del excel de panel
    archivo = pd.read_excel("Listas/panel.xls")

    lista = []
    Documentos = []
    Condicion = []
    columnas = archivo.columns
    columnas = columnas.tolist()
    valores = archivo.values

    val = archivo[columnas[1]]
    for elemento in val:
        elemento = str(elemento)
        Documentos.append(elemento)

    val = archivo[columnas[4]]
    for elemento in val:
        elemento = str(elemento)
        Condicion.append(elemento)

    # Crea una lista de tuplas de la forma (dni, condicion)
    ListaPanel = []
    i = 0
    while i != len(Documentos):
        tupla = (Documentos[i], Condicion[i])
        ListaPanel.append(tupla)
        i += 1

    # separa la lista de panel en lista de aprobados y Reprobados
    AprobadosPanel = []
    ReprobadosPanel = []

    crearListasAR(ListaPanel, AprobadosPanel, ReprobadosPanel)

    # ================================COMPROBAR PANEL/DRIVE===================================
    # Aprobados
    AprobadosDrive = []
    ReprobadosDrive = []

    # Extrae los documentos y condiciones finales del excel de Drive
    archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=0)

    AprobadosDrive = []
    columnas = archivo.columns
    columnas = columnas.tolist()
    valores = archivo.values

    val = archivo[columnas[0]]
    for elemento in val:
        elemento = str(elemento)
        AprobadosDrive.append(elemento)

    # Reprobados
    archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=1)

    ReprobadosDrive = []
    columnas = archivo.columns
    columnas = columnas.tolist()
    valores = archivo.values

    val = archivo[columnas[0]]
    for elemento in val:
        elemento = str(elemento)
        ReprobadosDrive.append(elemento)

    # ================Verificación================

    # Aprobados que están reprobados en Panel
    aNoPanel = noEncontrados(AprobadosDrive, AprobadosPanel)
    # Aprobados que están reprobados en Drive
    aNoDrive = noEncontrados(AprobadosPanel, AprobadosDrive)
    # Reprobados que están aprobados en panel
    rNoPanel = noEncontrados(ReprobadosDrive, ReprobadosPanel)
    # Reprobados que están aprobados en panel
    rNoDrive = noEncontrados(ReprobadosPanel, ReprobadosDrive)

    totalPanel = AprobadosPanel + ReprobadosPanel
    totalDrive = AprobadosDrive + ReprobadosDrive

    # ======================================================================================================================
    #                                               Mostrar Resultados
    # ======================================================================================================================

    if len(totalPanel) > len(totalDrive):
        diferencia = len(totalPanel) - len(totalDrive)
        print("Hay " + str(diferencia) + " participantes que no están en drive. Estos son: ")
        print(noEncontrados(totalPanel, totalDrive))
    elif len(totalDrive) > len(totalPanel):
        diferencia = len(totalDrive) - len(totalPanel)
        print("Hay " + str(diferencia) + " participantes que no están en panel. Estos son:")
        print(noEncontrados(totalDrive, totalPanel))

    # ------------ Comprobación de Aprobados -----------------
    if listasIguales(AprobadosDrive, AprobadosPanel):
        print("Los Aprobados de Drive/Panel son correctos.")
    else:
        if len(aNoPanel) != 0:
            print("Los siguientes participantes no se encuentran en panel: ")
            print(aNoPanel)

        if len(aNoDrive) != 0:
            print("Los siguientes participantes no se encuentran en panel: ")
            print(aNoDrive)

    # ------------ Comprobación de Reprobados -----------------
    if listasIguales(ReprobadosDrive, ReprobadosPanel):
        print("Los Reprobados de Drive/Panel son correctos.")
    else:
        if len(rNoPanel) != 0:
            print("Los siguientes participantes no se encuentran en panel: ")
            print(rNoPanel)

        if len(rNoDrive) != 0:
            print("Los siguientes participantes no se encuentran en panel: ")
            print(rNoDrive)

    print("Todo listo!")