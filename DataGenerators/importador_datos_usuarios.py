import pandas as pd
import sqlite3

# Nombre del archivo Excel generado
file_name = "usuarios_faker.xlsx"

# Ruta al archivo de base de datos (está en el mismo directorio que el script)
db_path = '../Proyecto/gestion_alquiler_autos.db'

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(file_name)

# Conectar a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Obtener el ID más alto existente en la tabla Usuario
cursor.execute("SELECT MAX(usuario_id) FROM Usuario")
max_id = cursor.fetchone()[0]

if max_id is None:
    max_id = 0  # Si la tabla está vacía, comienza desde 0

# Generar nuevos usuario_id a partir del siguiente número
df['usuario_id'] = range(max_id + 1, max_id + 1 + len(df))

# Convertir todas las demás columnas a string para asegurar compatibilidad con TEXT
for col in df.columns:
    if col != 'usuario_id':  # Excluir 'usuario_id' de la conversión
        df[col] = df[col].astype(str)

# Nombre de la tabla específica donde quieres insertar los datos
table_name = 'Usuario'

# Verificar que la tabla existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
if cursor.fetchone() is None:
    print(f"La tabla '{table_name}' no existe en la base de datos.")
    conn.close()
    exit()

# Insertar los datos en la tabla específica
for i, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (usuario_id, nombre, apellido, email, password, telefono, direccion, tipo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(row))

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()

print(f"Datos importados correctamente desde {file_name} a la tabla '{table_name}' en '{db_path}'.")


