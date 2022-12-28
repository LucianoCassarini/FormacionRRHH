
#! Solo realizar cambios en este archivo en caso de que haya cambios en el formato de las listas
#******************************************************************************
#******************************************************************************
#*              A CONTINUACIÓN PUEDE CAMBIAR LOS VALORES DE 
# *                 LAS VARIABLES DE LOS DOCUMENTOS DE:
#******************************************************************************
#******************************************************************************

# Los numeros refieren al numero de la columna en drive empezando a contar desde 0.

#! ================================ DRIVE =====================================
columna_dni_drive = 0
columna_apellido_drive = 1
columna_nombre_drive = 2
columna_correo_drive = 3
columna_condicion_drive = 12 #APROBADO/REPROBADO

separador_comision_drive = " " #Indica qué hay antes de la comisión en el nombre de la hoja de drive.
# Un ejemplo de nombre de hoja en drive es PolisPen_C1 por lo tanto el separador es "_".

nombre_hoja_esqueleto_drive = "Hoja Esqueleto" #En caso de no existir una hoja esqueleto ignorar esta variable

#? ---------- Colores -----------
rojo_no_encontrados = 'FFFF0000'  # ! -> No encontrados
gris_final_lista = 'FFD9D9D9'  # ? -> Fin de la lista


#! ================================ PANEL =====================================
columna_dni_panel = 1
columna_apellido_panel = 2
columna_correo_panel = 12
columna_condicion_panel = 4

#! ============================== Certificados ================================
#En caso de que en un futuro los certificados cambien puede que el DNI ya no se encuentre en la posición correcta,
# pueden cambiar la siguiente variable para indicar su posición.

# El script extrae todos los numeros del pdf, por ende si el DNI es el 3er nupero en aparecer su posición será la 2
# ya que se empieza a contar desde 0.
posicion_dni = 0