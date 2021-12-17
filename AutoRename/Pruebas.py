import os
import AuxFunc
import pandas as pd
#============================================Comparar Reprobados==============================================
archivo = pd.read_excel("ReprobadosPanel.xlsx")

lista = []
Reprobados = []
columnas = archivo.columns
columnas = columnas.tolist()
valores = archivo.values

val = archivo[columnas[0]]
for elemento in val:
    elemento = str(elemento)
    Reprobados.append(elemento)

# print(Reprobados)
# print(len(Reprobados))

# #devuelve directorio del programa
saved_path = os.getcwd()

# Crea lista de nombres del directorio
file_list = AuxFunc.nameList(saved_path + "/CorrectName")

Documentos = []

for file in file_list:
    doc = file.split("_")[0]
    Documentos.append(doc)

# print(Documentos)
print("Se encontraron " + str(len(Documentos)) + " certificados. \n")

CertificadosReprobados = []
for reps in Reprobados:
    for doc in Documentos:
        if doc == reps:
            CertificadosReprobados.append(doc)

print("Los Siguientes participantes están reprobados: ")
print(CertificadosReprobados)
print("Hay " + str(len(CertificadosReprobados)) + " Reprobados.\n")

#============================================Comparar Aprobados==============================================
archivoA = pd.read_excel("AprobadosPanel.xlsx")

listaA = []
Aprobados= []
columnasA = archivoA.columns
columnasA = columnasA.tolist()
valoresA = archivo.values

valA = archivoA[columnas[0]]
for elemento in valA:
    elemento = str(elemento)
    Aprobados.append(elemento)

#Elimina el .0
listaSinCero = []
for elemento in Aprobados:
    if elemento != "nan":
        doc = elemento.split(".")[0]
        listaSinCero.append(doc)

Aprobados = listaSinCero

print("Aprobados :" + str(len(Aprobados)))
print(Aprobados)
print("\n")

Viejos = []
for dni in Documentos:
    if dni not in Aprobados:
        if dni not in Reprobados:
            Viejos.append(dni)

FaltanCertificar = []
for doc in Aprobados:
    if doc not in Documentos:
        FaltanCertificar.append(doc)

print("Hay " + str(len(Viejos)) +" Que no estn en drive")
print(Viejos)
print("\n")

print("Faltan Certificar " + str(len(FaltanCertificar)) + " Participantes Aprobados.")
print(FaltanCertificar)
print("\n")

#============================================Comprobar Repetidos==============================================
listaLimpia = []
listaRepetidos = []
for dni in Documentos:
    if dni not in listaLimpia:
        listaLimpia.append(dni)
    else:
        listaRepetidos(dni)

print("hay " + str(len(listaRepetidos)) + " Repetidos.")


# ======================================Dulicados========================================
# # #devuelve directorio del programa
# saved_path = os.getcwd()
#
# # Crea lista de nombres del directorio
# file_list = AuxFunc.nameList(saved_path + "/CorrectName")
#
# mover = []
#
# for dni in Repetidos:
#     for file in file_list:
#         doc = file.split("_")[0]
#
#         if doc == dni:
#             mover.append(file)
#
# flag = ""
# for name in mover:
#     doc = name.split("_")[0]
#     if flag == doc:
#         file = saved_path + "/CorrectName/" + name
#         saveNew = saved_path + "/Duplicados/" + doc
#         os.rename(file, saveNew)
#     else:
#         flag = doc


