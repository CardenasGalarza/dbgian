from setuptools import setup, find_packages

setup(
    name='dbgian',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Aquí puedes agregar las dependencias si las tienes
    ],
    entry_points={
        'console_scripts': [
            'dbgian = dbgian:main',  # Asegúrate de que el nombre del módulo sea correcto
        ],
    },
    description='Una breve descripción de tu paquete.',
    long_description='Descripción más detallada, instrucciones de uso, etc.',
    author='Giancarlos Cardenas Galarza',
    author_email='alex10estadistica@gmail.com',
    url='https://github.com/CardenasGalarza/dbgian.git',
)
