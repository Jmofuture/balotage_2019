from package import constants as c
from package import balotage as bl
from package import base as b


df_balotage = bl.import_balotage(c.URL_BALOTAGE, c.DEPARTMENTS, c.DATE, c.COLUMNS)

bl.create_csv(df_balotage)

con = b.connection_db(c.CONFIG_DB)

b.create_database(con, c.DB_NAME)

table_query = b.query_create_table(c.TYPE_MAPPING,df_balotage, c.DB_NAME)

b.create_table(con, table_query,c.DB_NAME)

b.insert_data(con, df_balotage, c.DB_NAME)

