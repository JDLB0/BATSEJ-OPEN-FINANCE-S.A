import sqlite3
import pandas as pd

def cargar_tabla(ruta_bd, nombre_tabla):
    """
    Carga una tabla de SQLite en un DataFrame de pandas.
    Args:
        ruta_bd (str): Ruta al archivo SQLite.
        nombre_tabla (str): Nombre de la tabla a cargar.
    Returns:
        pd.DataFrame: Datos de la tabla como DataFrame.
    """
    conexion = sqlite3.connect(ruta_bd)
    query = f"SELECT * FROM {nombre_tabla}"
    datos = pd.read_sql_query(query, conexion)
    conexion.close()
    return datos
