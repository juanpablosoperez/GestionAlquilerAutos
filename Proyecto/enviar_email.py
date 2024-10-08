import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


def enviar_correo_confirmacion(email):
    # Configuración del servidor SMTP y credenciales
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = 'soperezjuanpablo1@gmail.com'
    smtp_password = 'h v r o v l e b p h s h j b r q'

    # Información del correo
    from_email = smtp_user
    to_emails = [email]
    subject = "Confirmación de registro"
    body = "Gracias por registrarte. Tu cuenta ha sido creada exitosamente!"

    # Crear el mensaje
    message = MIMEMultipart()
    message["From"] = 'Gestión de Alquileres de Autos'
    message["To"] = ", ".join(to_emails)
    message["Subject"] = subject

    # Adjuntar el cuerpo del correo
    message.attach(MIMEText(body, "plain"))

    start_time = time.time()

    server = None

    # Enviar el correo
    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        # Enviar el correo
        text = message.as_string()
        server.sendmail(from_email, to_emails, text)

        end_time = time.time()

        print("Correo enviado con éxito.")
        print(f"Tiempo de envío: {end_time - start_time:.2f} segundos")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        if server is not None:
            server.quit()


def enviar_correo_confirmacion_pago(email):
    # Configuración del servidor SMTP y credenciales
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = 'soperezjuanpablo1@gmail.com'
    smtp_password = 'h v r o v l e b p h s h j b r q'

    # Información del correo
    from_email = smtp_user
    to_emails = [email]
    subject = "Confirmación de Pago"
    body = "Gracias por confiar en nosotros. Tu pago ha sido realizado exitosamente!"

    # Crear el mensaje
    message = MIMEMultipart()
    message["From"] = 'Gestión de Alquileres de Autos'
    message["To"] = ", ".join(to_emails)
    message["Subject"] = subject

    # Adjuntar el cuerpo del correo
    message.attach(MIMEText(body, "plain"))

    start_time = time.time()

    # Inicializar server
    server = None

    # Enviar el correo
    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        # Enviar el correo
        text = message.as_string()
        server.sendmail(from_email, to_emails, text)

        end_time = time.time()

        print("Correo enviado con éxito.")
        print(f"Tiempo de envío: {end_time - start_time:.2f} segundos")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        if server is not None:
            server.quit()

