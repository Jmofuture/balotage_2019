import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(".env")


config = {
  'user': os.getenv('USER_MYSQL'),
  'password': os.getenv('PASSWORD_MYSQL'),
  'host': os.getenv('HOST'),
  'raise_on_warnings': True
}


try:
    con = mysql.connector.connect(**config)
    print("Connected")
except Exception as e:
    print(f"{e}")

con.close()



"""
query = 
    IF NOT EXIST CREATE TABLE balotage (
    Fecha_carga date,
    Departamento_ISO VARCHAR(2),
    Departamento VARCHAR(20),
    Total_Habilitados smallint,
    Total_Votos_Emitidos smallint,
    Total_Votos_NO_Observados smallint,
    Total_Votos_Observados smallint,
    Total_Anulados smallint,
    Total_EN_Blanco smallint,
    Total_Martinez_Villar smallint,
    Total_Lacalle Pou_Argimon int
    );
    

data = supabase.raw(query).execute()
"""
