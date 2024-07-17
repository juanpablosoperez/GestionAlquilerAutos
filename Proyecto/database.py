import sqlite3


def obtener_conexion_bd():
    # Conectar a la base de datos existente
    conn = sqlite3.connect('C:\\Users\\JUAMPI\\Documents\\Desarrollo de Software\\2DO AÑO D. SOFTWARE\\Programacion I\\Gestion de Alquiler Autos\\gestion_alquiler_autos.db')
    return conn


def crear_usuario(nombre_usuario, contrasena, tipo_usuario):
    conn = obtener_conexion_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Usuario (nombre, password, tipo) VALUES (?, ?, ?)", (nombre_usuario, contrasena, tipo_usuario))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True


def verificar_usuario(nombre_usuario, contrasena):
    conn = obtener_conexion_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario WHERE nombre = ? AND password = ?", (nombre_usuario, contrasena))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None


def inicializar_admin():
    if not verificar_usuario('admin', 'admin'):
        crear_usuario('admin', 'admin', 'administrador')
