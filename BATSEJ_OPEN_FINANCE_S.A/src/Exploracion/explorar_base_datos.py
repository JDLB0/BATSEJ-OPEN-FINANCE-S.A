import sqlite3

def explorar_base_datos(ruta_bd):
    """
    Explora la base de datos SQLite y muestra sus tablas y datos iniciales.
    Args:
        ruta_bd (str): Ruta al archivo SQLite.
    """
    try:
        conexion = sqlite3.connect(ruta_bd)
        cursor = conexion.cursor()

        # Ver las tablas disponibles
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")

        # Mostrar los primeros registros de cada tabla
        for tabla in tablas:
            print(f"\nDatos de la tabla '{tabla[0]}':")
            cursor.execute(f"SELECT * FROM {tabla[0]} LIMIT 5;")
            filas = cursor.fetchall()
            for fila in filas:
                print(fila)

        conexion.close()

    except sqlite3.Error as e:
        print(f"Error al explorar la base de datos: {e}")

# Ruta a tu base de datos
ruta_base_datos = "C:/Users/juand/OneDrive/Documentos/Prueba Analista/BATSEJ_OPEN_FINANCE_S.A/data/database.sqlite"
explorar_base_datos(ruta_base_datos)
