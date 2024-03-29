import os
from datetime import date as d
from dotenv import load_dotenv

DATE = d.today()


URL_BALOTAGE = "https://catalogodatos.gub.uy/dataset/8a20dcc5-77c7-499d-9932-5d0ebea4df37/resource/a71df2ea-b075-40e7-80b5-1df4c781bb99/download/balotaje-2019.csv"


DEPARTMENTS = {'AR':'Artigas',
'CA':'Canelones',
'CL':'Cerro Largo',
'CO':'Colonia',
'DU':'Durazno',
'FS':'Flores',
'FD':'Florida',
'LA':'Lavalleja',
'MA':'Maldonado',
'MO':'Montevideo',
'PA':'Paysandú',
'RN':'Río Negro',
'RV':'Rivera',
'RO':'Rocha',
'SA':'Salto',
'SJ':'San José',
'SO':'Soriano',
'TA':'Tacuarembó',
'TT':'Treinta y Tres'}



COLUMNS=['Fecha_carga','Departamento_ISO', 'Departamento','Total_Habilitados','Total_Votos_Emitidos', 'Total_Votos_NO_Observados',
         'Total_Votos_Observados', 'Total_Anulados', 'Total_EN_Blanco',
       'Total_Martinez_Villar', 'Total_Lacalle Pou_Argimon'] 



load_dotenv(".env")


CONFIG_DB = {
  'user': os.getenv('USER_MYSQL'),
  'password': os.getenv('PASSWORD_MYSQL'),
  'host': os.getenv('HOST'),
  'raise_on_warnings': True
}

DB_NAME = 'balotage'


TYPE_MAPPING = {
    'object': 'VARCHAR(255)',
    'int64': 'INT',
    'float64': 'FLOAT',
    'datetime64[ns]': 'TIMESTAMP',
    'bool': 'BOOLEAN'
}