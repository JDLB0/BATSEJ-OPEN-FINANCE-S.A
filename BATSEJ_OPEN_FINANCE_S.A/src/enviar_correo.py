import win32com.client as win32
import os

def enviar_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    """
    Envía un correo electrónico utilizando Microsoft Outlook con opción de adjuntar archivo.

    Esta función utiliza la API de Windows COM para interactuar con Outlook y enviar correos.
    Requiere que Outlook esté instalado y configurado en el sistema.

    Args:
        receptor (str): Dirección de correo electrónico del destinatario.
            Puede incluir múltiples direcciones separadas por punto y coma (;).
        asunto (str): Línea de asunto del correo electrónico.
        cuerpo (str): Contenido del mensaje en formato texto plano.
        ruta_adjunto (str, optional): Ruta completa al archivo que se desea adjuntar.
            Por defecto es None (sin adjuntos).
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
