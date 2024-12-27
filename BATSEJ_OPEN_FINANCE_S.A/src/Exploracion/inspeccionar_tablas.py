import sqlite3

def inspeccionar_tablas(ruta_bd):
    """
    Realiza un análisis detallado de la estructura de todas las tablas en una base de datos SQLite.

    Esta función examina cada tabla en la base de datos y proporciona información detallada
    sobre su estructura, incluyendo nombres de columnas, tipos de datos y claves primarias.
    Es útil para entender el esquema completo de la base de datos.

    Args:
        ruta_bd (str): Ruta completa al archivo de base de datos SQLite.
            Ejemplo: 'C:/ruta/hacia/base_datos.sqlite'

    Raises:
        sqlite3.Error: Si ocurre algún error durante la conexión o consulta a la base de datos.
            Esto puede incluir:
            - Error de archivo no encontrado
            - Error de permisos
            - Error de formato de base de datos
            - Error en la ejecución de consultas

    Output:
        Imprime en consola para cada tabla:
        1. Nombre de la tabla
        2. Para cada columna:
           - Nombre de la columna
           - Tipo de dato
           - Indicador de clave primaria
    Note:
        La función utiliza la tabla sistema PRAGMA table_info para obtener
        la información detallada de las columnas, lo que proporciona la
        información más precisa sobre la estructura de la base de datos.
    """
    try:
        conexion = sqlite3.connect(ruta_bd)
        cursor = conexion.cursor()

        # Ver todas las tablas de la base de datos
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        print("Tablas encontradas en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")

        # Inspeccionar cada tabla
        for tabla in tablas:
            print(f"\nEstructura de la tabla '{tabla[0]}':")
            cursor.execute(f"PRAGMA table_info({tabla[0]});")
            columnas = cursor.fetchall()
            for columna in columnas:
                print(f"Columna: {columna[1]}, Tipo: {columna[2]}, ¿Es clave primaria?: {'Sí' if columna[5] == 1 else 'No'}")

        conexion.close()

    except sqlite3.Error as e:
        print(f"Error al inspeccionar las tablas: {e}")

# Ruta a la base de datos
ruta_base_datos = "C:/Users/juand/OneDrive/Documentos/Prueba Analista/BATSEJ_OPEN_FINANCE_S.A/data/database.sqlite"
inspeccionar_tablas(ruta_base_datos)
