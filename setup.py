from setuptools import setup, find_packages

setup(
    name='BalotajeETL',
    version='0.1.0',
    description='Proyecto de ETL para el análisis de datos del balotaje de 2019 en Uruguay',
    author='Jean Olmedillo',
    packages=find_packages(),
install_requires=[
    'python-dotenv',
    'mysql-connector-python',
    'pandas'
]

)