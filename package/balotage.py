import pandas as pd

def import_balotage(url_balotage, departments, date, columns):

    df_balotage = pd.read_csv(url_balotage)
    df_balotage.rename(columns={"Departamento": "Departamento_ISO"}, inplace=True)
    df_balotage["Departamento"] = df_balotage["Departamento_ISO"].map(departments)
    df_balotage["Fecha_carga"] = date
    df_balotage = df_balotage[columns]
    df_balotage.rename(columns={'Total_Lacalle Pou_Argimon': 'Total_Lacalle_Pou_Argimon'}, inplace=True)

    print(df_balotage.head())

    return df_balotage



