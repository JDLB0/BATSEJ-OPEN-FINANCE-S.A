from cargar_db import cargar_tabla
from calcular_comision import calcular_comisiones
from generar_reportes import generar_reporte_excel
from enviar_correo import enviar_correo_outlook
import os
from datetime import datetime

def obtener_ruta_base():
    """
    Encuentra la ruta base del proyecto buscando la carpeta 'Prueba Analista'.
    Returns:
        str: Ruta base del proyecto.
    """
    ruta_actual = os.getcwd()
    while not os.path.basename(ruta_actual).upper() == "BATSEJ-OPEN-FINANCE-S.A":
        ruta_actual = os.path.dirname(ruta_actual)
        if ruta_actual == os.path.dirname(ruta_actual):  # Llegamos a la raíz
            raise FileNotFoundError("No se encontró la carpeta 'BATSEJ-OPEN-FINANCE-S.A'.")
    return ruta_actual

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n--- Menú de Opciones ---")
    print("1. Cargar datos de la base de datos")
    print("2. Calcular comisiones")
    print("3. Generar reporte en Excel")
    print("4. Enviar reporte por correo")
    print("5. Salir")
    print("------------------------")

def main():
    
    datos_apicall = None
    datos_commerce = None
    reporte = None

    ruta_base = obtener_ruta_base()

    ruta_bd = os.path.join(ruta_base, "BATSEJ_OPEN_FINANCE_S.A", "data", "database.sqlite")

    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M")  # Formato: 20241226_0213
    ruta_reporte = os.path.join(ruta_base, "Salidas", f"reporte_comisiones_{fecha_hora}.xlsx")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nCargando datos de la base de datos...")
            datos_apicall = cargar_tabla(ruta_bd, 'apicall')
            datos_commerce = cargar_tabla(ruta_bd, 'commerce')
            print("Datos cargados exitosamente.")
            print(f"Transacciones (apicall): {len(datos_apicall)} registros")
            print(f"Comercios (commerce): {len(datos_commerce)} registros")

        elif opcion == "2":
            if datos_apicall is not None and datos_commerce is not None:
                print("\nCalculando comisiones...")
                reporte = calcular_comisiones(datos_apicall, datos_commerce)
                print("Comisiones calculadas exitosamente.")
                print("\nResumen de las primeras filas:")
                print(reporte.head()) 
            else:
                print("\nPor favor, carga los datos primero (opción 1).")

        elif opcion == "3":
            if reporte is not None:
                print("\nGenerando reporte en Excel...")
                generar_reporte_excel(reporte, ruta_reporte)
                print(f"Reporte generado exitosamente en: {ruta_reporte}")
            else:
                print("\nPor favor, calcula las comisiones primero (opción 2).")

        elif opcion == "4":
            if reporte is not None:
                print("\nEnviando reporte por correo...")
                ejecutor = input("Ingresa el correo de destino de la informacion del reporte: ")
                asunto = "Reporte de Comisiones"
                cuerpo = (
                    "Buena tarde, la informacion que encontrarás sobre el reporte de comisiones generado por tu empresa, "
                    "con la estructura solicitada: Fecha-Mes, Nombre, Nit, "
                    "Valor_comision, Valor_iva, Valor_Total, Correo."
                )
                enviar_correo_outlook(ejecutor, asunto, cuerpo, ruta_reporte)
            else:
                print("\nPor favor, genera el reporte primero (opción 3).")

        elif opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
