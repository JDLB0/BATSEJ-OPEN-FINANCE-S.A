import pandas as pd
import xlsxwriter

def generar_reporte_excel(reporte, nombre_archivo):
    """
    Genera un archivo Excel con el reporte de comisiones.
    """
    with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
        reporte.to_excel(writer, index=False, sheet_name='Reporte')