# Step by Step crear un paquete ditribuible

*Para visualizar markdown con el plugin CTRL + Shift + P*


Para crear un paquete ditribuible, tenemos que crear un fichero
llamado setup.py fuera en la raiz donde tenemos nuestro script.
Crearemos el fichero y definiremos una información básica con información de este pquete

`from setuptools import setup`

`setup(
	name="paquete",
	version="0.1",
	description="Este es un paquete de ejemplo",
	author="Érika Cebriá",
	author_email="erika.c.caballero@gmail.com",
	url="http://e-creaweb.com",
	# Si quisiera integrar dentro del paquete algun script
	scripts=[],
    packages=['paquete','paquete.hola','paquete.adios']
)`

## Para crear el paquete distribuible

Una vez tenemos definido el distribuible, con su info básica incluyendo paquetes y subpaquetes.

Ahora tenemos que crear el distribuible, un fichero que podremos instalar o enviar para que lo instalen.

1. Ir al directorio donde tenemos el `setup.py` y el paquete.
2. Abrir con la terminal Shift + click dcho -> abrir ventana de comando aquí.
3. Crear el distribuible llamando a Python, setup.py que es el fichero que acabmos de crear, y con el comando sdist para crear un distribuible.
4. Se habrá creado un zip en el directorio

	* Ejecutar en terminal  paso 3
	`python setup.py sdist`

	* Salida 
`running sdist
running egg_info
creating paquete.egg-info
writing paquete.egg-info\PKG-INFO
writing dependency_links to paquete.egg-info\dependency_links.txt
writing top-level names to paquete.egg-info\top_level.txt
writing manifest file 'paquete.egg-info\SOURCES.txt'
reading manifest file 'paquete.egg-info\SOURCES.txt'
writing manifest file 'paquete.egg-info\SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt
running check
creating paquete-0.1
creating paquete-0.1\paquete
creating paquete-0.1\paquete.egg-info
creating paquete-0.1\paquete\adios
creating paquete-0.1\paquete\hola
copying files to paquete-0.1...
copying setup.py -> paquete-0.1
copying paquete\__init__.py -> paquete-0.1\paquete
copying paquete\saludos.py -> paquete-0.1\paquete
copying paquete.egg-info\PKG-INFO -> paquete-0.1\paquete.egg-info
copying paquete.egg-info\SOURCES.txt -> paquete-0.1\paquete.egg-info
copying paquete.egg-info\dependency_links.txt -> paquete-0.1\paquete.egg-info
copying paquete.egg-info\top_level.txt -> paquete-0.1\paquete.egg-info
copying paquete\adios\__init__.py -> paquete-0.1\paquete\adios
copying paquete\adios\despedidas.py -> paquete-0.1\paquete\adios
copying paquete\hola\__init__.py -> paquete-0.1\paquete\hola
copying paquete\hola\saludos.py -> paquete-0.1\paquete\hola
Writing paquete-0.1\setup.cfg
creating dist
Creating tar archive
removing 'paquete-0.1' (and everything under it)`

**NOTA** 
Powershell me crea un tar como e Linux

## Para instalar el paquete distribuible

1. Mediante la consola, desde cualquier directorio donde esté distribuible, nos introducimos en el directorio dist
2. Ejecutamos el comando `pip3 install paquete-0.1.tar.gz`, 
si no funciona `pip3` utilizar `pip`.
3. Se instalará el paquete.
4. Para cosnultar la lista de paquetes instalados; `pip3 list` o `pip list`
5. Si queremos ejecutar el fichero script.py podemos ejecutar desde cualquier dirctorio funcionará.

## Para desinstalr un paquete

Ejecutamos el comando `pip3 unistall paquete-0.1.tar.gz` 