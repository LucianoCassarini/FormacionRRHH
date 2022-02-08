#__________________ Comprueba que la acción sea valida _________________
def comprobarAccion(LAcciones, accion):

    flag = False

    if int(accion) > len(LAcciones) or int(accion) < 1:
        print("ERROR: La acción seleccionada no es valida.\n")
    else:
        print("Se seleccionó la acción " + str(LAcciones[int(accion)-1][1]))
        flag = True

    return  flag

#___________________ Seleccionar Una opción valida ____________________
def seleccionarAcción(LAcciones):
    accion = input("Seleccione una acción: ")
    validacion = comprobarAccion(LAcciones, accion)
    if validacion == False:
        while validacion != True:
            accion = input("Por favor vuelva a seleccionar una acción: ")
            validacion = comprobarAccion(LAcciones, accion)

    return accion

#______ Llamar a la función correspondiente dependiendo de la acción seleccionada ________
#def ejecutarAccion(accion):


print('''
███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░███╗░░██╗░░░██████╗░██████╗░██╗░░██╗██╗░░██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗████╗░██║░░░██╔══██╗██╔══██╗██║░░██║██║░░██║
█████╗░░██║░░██║██████╔╝██╔████╔██║███████║██║░░╚═╝██║██║░░██║██╔██╗██║░░░██████╔╝██████╔╝███████║███████║
██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██║░░██║██║╚████║░░░██╔══██╗██╔══██╗██╔══██║██╔══██║
██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║██╗██║░░██║██║░░██║██║░░██║██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝ \n''')

print("Lista de acciónes: \n")
LAcciones = [(1, "RenombrarCertificados"), (2, "BuscarErrores")]

print("[1]. Renombrar certificados.")
print("[2]. Busqueda de errores (Drive/Panel).")

accion = seleccionarAcción(LAcciones)


