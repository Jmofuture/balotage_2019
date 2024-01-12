import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(dotenv_path=".env")

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")


try:
    supabase: Client = create_client(url, key)
    print("Connected")
except Exception as e:
    print(f"Error: {e}")



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




"""

import psycopg2

# Conectarse a la base de datos de PostgreSQL
conn = psycopg2.connect(
    dbname="tu_dbname",
    user="tu_usuario",
    password="tu_contraseña",
    host="tu_host_de_supabase"
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar una consulta SQL
cur.execute("
    CREATE TABLE mi_tabla (
        id SERIAL PRIMARY KEY,
        columna1 VARCHAR(255),
        columna2 INT
    );
")

# Confirmar la transacción
conn.commit()

# Cerrar el cursor y la conexión
cur.close()
conn.close()

"""