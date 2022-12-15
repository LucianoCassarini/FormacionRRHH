import pandas as pd
import Global
from time import sleep
from progress.bar import ChargingBar

#---- Separar en listas de aprobados y reprobados de panel ----
def crearListasAR(listaPanel, lAprobados, lReprobados):
    for participante in listaPanel:
        dni = participante[0]
        correo = participante[1]
        condicion = participante[2]
        if condicion == "APROBADO":
            lAprobados.append((dni, correo))
        elif condicion == "REPROBADO":
            lReprobados.append((dni, correo))


#------ Devuelve los elementos que no estan en ambas listas -------
def noEncontrados(lista1, lista2):
    listaNoEncontrados = []

    for participante in lista1:
        flag = False
        for participanteAux in lista2:
            if participanteAux[0] == participante[0]:
                flag = True
            elif participanteAux[1] == participante[1]:
                flag = True
        if flag == False:
            listaNoEncontrados.append(participante)

    return listaNoEncontrados


#======================================================================================================================
#                                                           RUN
#======================================================================================================================
def ValidarErroresDrivePanel():
    
    print("Comprobando listas de Drive y Panel...")
    # Extrae los documentos y condiciones finales del excel de panel
    archivo = pd.read_excel("Listas/panel.xls")
    
    bar1 = ChargingBar('', max=5)
    bar1.next()
    
    Documentos = []
    Correos = []
    Condicion = []
    columnas = archivo.columns
    columnas = columnas.tolist()

    val = archivo[columnas[Global.columna_dni_panel]]
    for elemento in val:
        elemento = str(elemento)
        Documentos.append(elemento)
        
    val = archivo[columnas[Global.columna_correo_panel]]
    for elemento in val:
        elemento = str(elemento)
        Correos.append(elemento)

    val = archivo[columnas[Global.columna_condicion_panel]]
    for elemento in val:
        elemento = str(elemento)
        Condicion.append(elemento)
        
    sleep(0.2)
    bar1.next()
    
    # Crea una lista de tuplas de la forma (dni, condicion)
    ListaPanel = []
    i = 0
    while i != len(Documentos):
        tupla = (Documentos[i], Correos[i], Condicion[i])
        ListaPanel.append(tupla)
        i += 1

    # separa la lista de panel en lista de aprobados y Reprobados
    AprobadosPanel = []
    ReprobadosPanel = []

    crearListasAR(ListaPanel, AprobadosPanel, ReprobadosPanel)
    
    sleep(0.2)
    bar1.next()

    # ================================COMPROBAR PANEL/DRIVE===================================
    #* ===========  Aprobados Drive ============
    AprobadosDrive = []
    ReprobadosDrive = []

    # Extrae los documentos y condiciones finales del excel de Drive
    archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=0)
    dniAprobados = []
    correoAprobados = []
    AprobadosDrive = []
    columnas = archivo.columns
    columnas = columnas.tolist()

    val = archivo[columnas[0]]
    for elemento in val:
        elemento = str(elemento)
        dniAprobados.append(elemento)
        
    val = archivo[columnas[3]]
    for elemento in val:
        elemento = str(elemento)
        correoAprobados.append(elemento)
    
    i = 0
    while i != len(dniAprobados):
        tupla = (dniAprobados[i], correoAprobados[i])
        AprobadosDrive.append(tupla)
        i += 1
        
    sleep(0.2)
    bar1.next()
    
    #* ============ Reprobados Drive  ============
    archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=1)
    dniReprobados = []
    correoReprobados = []
    columnas = archivo.columns
    columnas = columnas.tolist()

    val = archivo[columnas[0]]
    for elemento in val:
        elemento = str(elemento)
        dniReprobados.append(elemento)
    
    val = archivo[columnas[3]]
    for elemento in val:
        elemento = str(elemento)
        correoReprobados.append(elemento)
    
    i = 0
    while i != len(dniReprobados):
        tupla = (dniReprobados[i], correoReprobados[i])
        ReprobadosDrive.append(tupla)
        i += 1
        
    sleep(0.2)
    bar1.next()
    
    # ================Verificación================

    # Aprobados que están reprobados en Panel
    aNoPanel = noEncontrados(AprobadosDrive, AprobadosPanel)
    # Aprobados que están reprobados en Drive
    aNoDrive = noEncontrados(AprobadosPanel, AprobadosDrive)
    # Reprobados que están aprobados en panel
    rNoPanel = noEncontrados(ReprobadosDrive, ReprobadosPanel)
    # Reprobados que están aprobados en panel
    rNoDrive = noEncontrados(ReprobadosPanel, ReprobadosDrive)

    totalPanel = len(AprobadosPanel) + len(ReprobadosPanel)
    totalDrive = len(AprobadosDrive) + len(ReprobadosDrive)

    # ======================================================================================================================
    #                                               Mostrar Resultados
    # ======================================================================================================================
    print("\n")

    # ------------ Comprobación de Aprobados -----------------
    if len(aNoDrive) == 0 & len(aNoPanel)==0:
        print("Los Aprobados de Drive/Panel son correctos.")
    elif len(rNoDrive) == 0 & len(rNoPanel)==0:
        print("Los Reprobados de Drive/Panel son correctos.")
    print("\n")
    
    if len(aNoPanel) != 0 or len(rNoPanel) != 0:
        print("Los siguientes participantes no se encuentran en panel: ")
        if len(aNoPanel) != 0:
            print(aNoPanel)
        if len(rNoPanel) != 0:
            print(rNoPanel)
        print("\n")
    
    if len(aNoDrive) != 0 or len(rNoDrive) != 0:
        print("Los siguientes participantes no se encuentran en drive: ")
        if len(aNoDrive) != 0:
            print(aNoDrive)
        if len(rNoDrive) != 0:
            print(rNoDrive)
    
    
    print("\n")
    print("Todo listo!")