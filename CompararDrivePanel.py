import os
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

#======================================================================================================================
#                                                           RUN
#======================================================================================================================

#Extrae los documentos y condiciones finales del excel de panel
archivo = pd.read_excel("Listas/Panel.xls")

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

#Crea una lista de tuplas de la forma (dni, condicion)
ListaPanel = []
i = 0
while i != len(Documentos):
    tupla = (Documentos[i], Condicion[i])
    ListaPanel.append(tupla)
    i += 1

#separa la lista de panel en lista de aprobados y Reprobados
AprobadosPanel = []
ReprobadosPanel = []

crearListasAR(ListaPanel, AprobadosPanel, ReprobadosPanel)

#================================COMPROBAR PANEL/DRIVE===================================
#Aprobados
AprobadosDrive = []
ReprobadosDrive = []

#Extrae los documentos y condiciones finales del excel de Drive
archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=0)

AprobadosDrive = []
columnas = archivo.columns
columnas = columnas.tolist()
valores = archivo.values

val = archivo[columnas[0]]
for elemento in val:
    elemento = str(elemento)
    AprobadosDrive.append(elemento)

#Reprobados
archivo = pd.read_excel("Listas/DriveProcesado.xlsx", sheet_name=1)

ReprobadosDrive = []
columnas = archivo.columns
columnas = columnas.tolist()
valores = archivo.values

val = archivo[columnas[0]]
for elemento in val:
    elemento = str(elemento)
    ReprobadosDrive.append(elemento)

#================Verificación================

#Aprobados que están reprobados en Panel
aNoPanel = []
#Aprobados que están reprobados en Drive
aNoDrive = []
#Reprobados que están aprobados en panel
rNoPanel = []
#Reprobados que están aprobados en panel
rNoDrive = []

#Comprovación de Aprobados
for aD in AprobadosDrive:
    flag = False
    for aP in AprobadosPanel:
        if aD == aP:
            flag = True
    if flag == False:
        aNoPanel.append(aD)

for aP in AprobadosPanel:
    flag = False
    for aD in AprobadosDrive:
        if aP == aD:
            flag = True
    if flag == False:
        aNoDrive.append(aP)

#Comprovación de Reprobados
for rD in ReprobadosDrive:
    flag = False
    for rP in ReprobadosPanel:
        if rD == rP:
            flag = True
    if flag == False:
        rNoPanel.append(rD)

for rP in ReprobadosPanel:
    flag = False
    for rD in ReprobadosDrive:
        if rP == rD:
            flag = True
    if flag == False:
        rNoDrive.append(rP)

totalPanel = len(AprobadosPanel) + len(ReprobadosPanel)
totalDrive = len(AprobadosDrive) + len(ReprobadosDrive)

if totalPanel != totalDrive:
    if totalPanel > totalDrive:
        diferencia = totalPanel - totalDrive
        print("Hay " + diferencia + " participantes que no están en drive.")
    elif totalDrive > totalPanel:
        diferencia = totalDrive - totalPanel
        print("Hay " + diferencia + " participantes que no están en panel.")