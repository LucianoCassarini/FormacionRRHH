# FormacionRRHH
#### Automatización de tareas - Ministerio de Economía - Santa Fe

###### Este script es capaz de:
- Procesar archivo de drive y separar en Aprobados y Reprobados.
- Comparar archivo de drive con archivo de panel en busca de posibles errores al calificar.
- Renombrar certificados de cursos de forma masiva.
- Detectar y corregir errores de certificación.

------------


##### Instalación de Dependencias:

> ###### Manualmente:
`pip3 install PyPDF2`

`pip3 install pandas`

`pip3 install openpyxl`

`pip3 install xlrd`

`pip3 install progress`

------------

#### En caso de no estar disponible la herramienta pip, esta puede instalarse de la siguiente forma:

# 


##### En Ubuntu (Para Python 3.x.x):
Instalar usando el comando:
`sudo apt update && sudo apt install python3-pip`

Cuando se complete la instalación, verificar la instalación y comprobar la versión instalada ejecutando el comando:
`pip3 --version`

# 


##### En Ubuntu (Para Python 2.x.x):
Para empezar, habrá que habilitar el repositorio universe:
`sudo add-apt-repository universe`

 Utilizando la herramienta curl, descargar el script get-pip.py:
 `curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py.`
 
 Terminada la descarga, ejecutar el script con python2 para instalar pip:
 `sudo python2 get-pip.py`
 
 Para verificar la versión utilizar el comando:
 `pip2 --version`


------------


> ###### Este script fue creado y testeado con versiones recientes de python se recomienda el uso de python 3.5 en adelante.


