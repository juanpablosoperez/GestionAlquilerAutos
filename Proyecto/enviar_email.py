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
    message["From"] = 'Gestión de Alquileres de Autos' # si no funciona pongo smtp_user
    message["To"] = ", ".join(to_emails)
    message["Subject"] = subject

    # Adjuntar el cuerpo del correo
    message.attach(MIMEText(body, "plain"))

    start_time = time.time()

    # Enviar el correo
    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar TLS
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
        server.quit()

# Ejemplo de uso:
# enviar_correo_confirmacion("juanpsoperez@gmail.com")

