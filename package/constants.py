from datetime import date as d

DATE = d.today()


URL_BALOTAGE = "https://catalogodatos.gub.uy/dataset/8a20dcc5-77c7-499d-9932-5d0ebea4df37/resource/a71df2ea-b075-40e7-80b5-1df4c781bb99/download/balotaje-2019.csv"


DEPARTMENTS = {'AR':'Artigas',
'CA':'Canelones',
'CL':'Melo',
'CO':'Colonia del Sacramento',
'DU':'Durazno',
'FS':'Trinidad',
'FD':'Florida',
'LA':'Minas',
'MA':'Maldonado',
'MO':'Montevideo',
'PA':'Paysandú',
'RN':'Fray Bentos',
'RV':'Rivera',
'RO':'Rocha',
'SA':'Salto',
'SJ':'San José de Mayo',
'SO':'Mercedes',
'TA':'Tacuarembó',
'TT':'Treinta y Tres'}



COLUMNS=['Fecha_carga','Departamento_ISO', 'Departamento','Total_Habilitados','Total_Votos_Emitidos', 'Total_Votos_NO_Observados',
         'Total_Votos_Observados', 'Total_Anulados', 'Total_EN_Blanco',
       'Total_Martinez_Villar', 'Total_Lacalle Pou_Argimon'
       ] 