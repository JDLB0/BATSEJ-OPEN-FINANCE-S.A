import sqlite3

def explorar_base_datos(ruta_bd):
    """
    Explora y muestra información básica sobre las tablas en una base de datos SQLite.

    Esta función se conecta a una base de datos SQLite, lista todas las tablas disponibles
    y muestra los primeros 5 registros de cada tabla para facilitar la exploración inicial
    de los datos.

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
        Imprime en consola:
        1. Lista de todas las tablas en la base de datos
        2. Primeros 5 registros de cada tabla encontrada
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
