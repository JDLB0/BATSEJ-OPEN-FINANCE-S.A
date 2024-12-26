import win32com.client as win32
import os

def enviar_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    """
    Envía un correo utilizando la cuenta configurada en Outlook.
    Args:
        receptor (str): Dirección de correo del receptor.
        asunto (str): Asunto del correo.
        cuerpo (str): Cuerpo del mensaje.
        ruta_adjunto (str, opcional): Ruta del archivo adjunto. Por defecto es None.
    """
    try:
        # Crear una instancia de la aplicación Outlook
        outlook = win32.Dispatch('outlook.application')

        # Crear un nuevo correo
        correo = outlook.CreateItem(0)
        correo.To = receptor
        correo.Subject = asunto
        correo.Body = cuerpo

        # Adjuntar archivo si se proporciona una ruta
        if ruta_adjunto and os.path.exists(ruta_adjunto):
            correo.Attachments.Add(ruta_adjunto)

        # Enviar el correo
        correo.Send()
        print(f"Correo enviado exitosamente a {receptor}.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
