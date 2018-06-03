from setuptools import setup

setup(
	name="paquete",
	version="0.1",
	description="Este es un paquete de jemplo",
	author="Érika Cebriá",
	author_email="erika.c.caballero@gmail.com",
	url="http://e-creaweb.com",
	# Si quisiera integrar dentro del paquete algun script
	scripts=[],
    packages=['paquete','paquete.hola','paquete.adios']
)