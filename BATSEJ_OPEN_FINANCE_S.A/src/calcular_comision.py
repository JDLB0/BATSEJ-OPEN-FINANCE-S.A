import pandas as pd
from datetime import datetime

def calcular_comisiones(datos_apicall, datos_commerce):
    """
    Calcula las comisiones según las reglas de cada empresa y prepara los datos para el correo.
    Filtra las empresas con estatus "Activo" y las peticiones de los meses julio y agosto de 2024.

    Args:
        datos_apicall (pd.DataFrame): Datos de las peticiones a la API.
        datos_commerce (pd.DataFrame): Información de las empresas.

    Returns:
        pd.DataFrame: Resumen de las comisiones calculadas con los nuevos campos.
    """
    # Filtrar empresas con estatus 'Activo'
    datos_commerce = datos_commerce[datos_commerce['commerce_status'] == 'Active']

    # Filtrar las peticiones de julio y agosto de 2024
    datos_apicall['date_api_call'] = pd.to_datetime(datos_apicall['date_api_call'])  # Asegurarse que la columna sea de tipo datetime
    datos_apicall = datos_apicall[
        (datos_apicall['date_api_call'].dt.month.isin([7, 8])) & 
        (datos_apicall['date_api_call'].dt.year == 2024)
    ]

    # Unir los datos de apicall con commerce para incluir nombres, NIT y correos
    datos_apicall = datos_apicall.merge(
        datos_commerce, 
        on='commerce_id', 
        how='left'
    )

    # Filtrar peticiones exitosas y no exitosas
    exitosas = datos_apicall[datos_apicall['ask_status'] == 'Successful'].copy()
    no_exitosas = datos_apicall[datos_apicall['ask_status'] != 'Successful'].copy()

    # Calcular comisiones por empresa
    def calcular_fila_comision(fila):
        empresa = fila['commerce_name']
        peticiones_exitosas = fila['Total_exitosas']
        peticiones_no_exitosas = fila['Total_no_exitosas']

        if empresa == "Innovexa Solutions":
            valor_comision = peticiones_exitosas * 300
        elif empresa == "NexaTech Industries":
            if peticiones_exitosas <= 10000:
                valor_comision = peticiones_exitosas * 250
            elif peticiones_exitosas <= 20000:
                valor_comision = peticiones_exitosas * 200
            else:
                valor_comision = peticiones_exitosas * 170
        elif empresa == "QuantumLeap Inc.":
            valor_comision = peticiones_exitosas * 600
        elif empresa == "Zenith Corp.":
            if peticiones_exitosas <= 22000:
                valor_comision = peticiones_exitosas * 250
            else:
                valor_comision = peticiones_exitosas * 130
            if peticiones_no_exitosas > 6000:
                valor_comision *= 0.95
        elif empresa == "FusionWave Enterprises":
            valor_comision = peticiones_exitosas * 300
            if 2500 <= peticiones_no_exitosas <= 4500:
                valor_comision *= 0.95
            elif peticiones_no_exitosas > 4500:
                valor_comision *= 0.92
        else:
            valor_comision = 0

        valor_iva = valor_comision * 0.19
        valor_total = valor_comision + valor_iva

        return pd.Series([valor_comision, valor_iva, valor_total], index=['Valor_comision', 'Valor_iva', 'Valor_Total'])

    # Calcular totales para cada empresa
    resumen = (
        exitosas.groupby(['commerce_id', 'commerce_name', 'commerce_nit'])
        .size()
        .reset_index(name='Total_exitosas')
    )

    no_exitosas_resumen = (
        no_exitosas.groupby(['commerce_id', 'commerce_name', 'commerce_nit'])
        .size()
        .reset_index(name='Total_no_exitosas')
    )

    resumen = resumen.merge(no_exitosas_resumen, on=['commerce_id', 'commerce_name', 'commerce_nit'], how='left').fillna(0)

    # Aplicar el cálculo de comisiones
    valores_comisiones = resumen.apply(calcular_fila_comision, axis=1)
    resumen[['Valor_comision', 'Valor_iva', 'Valor_Total']] = valores_comisiones

    # Agregar la columna 'Fecha-Mes' con el formato actual
    fecha_mes = datetime.now().strftime("%Y-%m")  # Formato: 2024-12
    resumen['Fecha-Mes'] = fecha_mes

    # Agregar la columna de 'Correo' que proviene de la tabla 'commerce'
    resumen = resumen.merge(
        datos_commerce[['commerce_id', 'commerce_email']], 
        on='commerce_id', 
        how='left'
    )
    resumen['Correo'] = resumen['commerce_email']

    # Renombrar las columnas 'commerce_name' y 'commerce_nit' a 'Nombre' y 'Nit'
    resumen = resumen.rename(columns={
        'commerce_name': 'Nombre',
        'commerce_nit': 'Nit'
    })

    # Reordenar las columnas según el formato solicitado
    resumen = resumen[['Fecha-Mes', 'Nombre', 'Nit', 'Valor_comision', 'Valor_iva', 'Valor_Total', 'Correo']]

    return resumen
