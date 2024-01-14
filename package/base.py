import mysql.connector

def connection_db(config):
    try:
        con = mysql.connector.connect(**config)
        print("Connected")
    except Exception as e:
        print(f"{e}")
    return con


def create_database(con, db_name):
    try:
        cursor = con.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
        result = cursor.fetchone()
        if not result:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Base de datos '{db_name}' creada.")
        else:
            print(f"La base de datos '{db_name}' ya existe.")
    except mysql.connector.Error as e:
        print(f"Failed creating database: {e}")
        exit(1)

def query_create_table(db_types,dataframe, table_name):
    columns = dataframe.columns
    column_types = dataframe.dtypes
    sql_columns = []

    for column, dtype in zip(columns, column_types):
        sql_dtype = db_types.get(str(dtype), 'VARCHAR(255)')
        sql_columns.append(f"{column} {sql_dtype}")

    column_str = ',\n    '.join(sql_columns)
    sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {column_str}\n);"
    print(sql_query)
    return sql_query

def create_table(con, query, database):
    cursor = con.cursor()
    cursor.execute(f"USE {database}")
    cursor.execute(query)
    con.commit()
    print("Tabla creada")

