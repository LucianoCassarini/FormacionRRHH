from ModuloCertificados import main
from ModuloCertificados import Validaciones
from ModuloDP import DriveGenerator
from ModuloDP import CompararDrivePanel

#__________________ Comprueba que la acción sea valida _________________

def comprobarAccion(LAcciones, accion):

    flag = False

    if int(accion) > len(LAcciones) or int(accion) < 1:
        print("ERROR: La acción seleccionada no es valida.\n")
    else:
        flag = True

    return flag

#___________________ Seleccionar Una opción valida ____________________
def seleccionarAccion(LAcciones):
    accion = input("Seleccione una acción: ")
    validacion = comprobarAccion(LAcciones, accion)
    if validacion == False:
        while validacion != True:
            accion = input("Por favor vuelva a seleccionar una acción: ")
            validacion = comprobarAccion(LAcciones, accion)

    return int(accion)


print("""
███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░███╗░░██╗░░░██████╗░██████╗░██╗░░██╗██╗░░██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗████╗░██║░░░██╔══██╗██╔══██╗██║░░██║██║░░██║
█████╗░░██║░░██║██████╔╝██╔████╔██║███████║██║░░╚═╝██║██║░░██║██╔██╗██║░░░██████╔╝██████╔╝███████║███████║
██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██║░░██║██║╚████║░░░██╔══██╗██╔══██╗██╔══██║██╔══██║
██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║██╗██║░░██║██║░░██║██║░░██║██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝ \n""")

print("Lista de acciónes: \n")
LAcciones = [(1, "Procesar archivo de drive"), (2, "Comprobar arrores (Drive/Panel)"),
             (3, "Renombrar certificados"), (4, "Buscar errores de certificación"), (5, "Salir")]

flag = True
while flag:
    print("[1]. Procesar archivo de drive. (Requiere el erchivo 'drive.xlsx')")
    print("[2]. Comparar listas Drive/Panel. (Requiere ejecutar acción 1 y archivo 'panel.xls')")
    print("[3]. Renombrar certificados.")
    print("[4]. Buscar errores de certifición. (Requiere archivo 'panel.xls')")
    print("[5]. Salir.\n")

    accion = seleccionarAccion(LAcciones)

    if accion == 5:
        flag = False

    if accion == 1:
        DriveGenerator.filtrarDrive()
        #Crear archivo drive
    elif accion == 2:
        CompararDrivePanel.ValidarErroresDrivePanel()
       #Comparar con panel
    elif accion == 3:
        main.Renombrar()
        #Renombrar certificados
    elif accion == 4:
        Validaciones.ValidarCertificados()
        #Buscar errores de certificación