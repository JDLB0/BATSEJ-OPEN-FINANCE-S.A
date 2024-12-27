import pandas as pd
import xlsxwriter

def generar_reporte_excel(reporte, nombre_archivo):
    """
    Genera un archivo Excel con el reporte de comisiones utilizando xlsxwriter.

    Esta función toma un DataFrame y lo exporta a un archivo Excel, manteniendo
    el formato y estructura de los datos originales.

    Args:
        reporte (pd.DataFrame): DataFrame conteniendo los datos del reporte.
            Debe incluir todas las columnas que se desean exportar al Excel.
        nombre_archivo (str): Ruta completa donde se guardará el archivo Excel.
            Ejemplo: 'C:/reportes/reporte_comisiones_202412.xlsx'

    Raises:
        PermissionError: Si el archivo está abierto o no se tiene permiso de escritura.
        Exception: Si hay problemas durante la generación del archivo Excel.

    Note:
        El archivo Excel generado no incluirá el índice del DataFrame y
        los datos se guardarán en una hoja llamada 'Reporte'.
    """
    with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
        reporte.to_excel(writer, index=False, sheet_name='Reporte')