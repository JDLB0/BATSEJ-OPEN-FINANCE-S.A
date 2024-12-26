import sqlite3

def inspeccionar_tablas(ruta_bd):
    """
    Inspecciona las tablas de la base de datos SQLite y muestra sus columnas y tipos de datos.
    Args:
        ruta_bd (str): Ruta al archivo SQLite.
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
