import pandas as pd
import sqlite3

# Nombre del archivo Excel generado
file_name = "reservas_faker.xlsx"

# Ruta al archivo de base de datos (está en el mismo directorio que el script)
db_path = 'gestion_alquiler_autos.db'

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(file_name)

# Convertir las columnas de fecha a formato 'YYYY-MM-DD'
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio']).dt.strftime('%Y-%m-%d')
df['fecha_fin'] = pd.to_datetime(df['fecha_fin']).dt.strftime('%Y-%m-%d')

# Valores permitidos para 'estado'
valid_states = {'Pendiente', 'Completada', 'Cancelada'}

# Filtrar datos con estados válidos
df = df[df['estado'].isin(valid_states)]

# Conectar a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Nombre de la tabla específica donde quieres insertar los datos
table_name = 'Reserva'

# Verificar que la tabla existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
if cursor.fetchone() is None:
    print(f"La tabla '{table_name}' no existe en la base de datos.")
    conn.close()
    exit()

# Insertar los datos en la tabla específica
for i, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (reserva_id, usuario_id, vehiculo_id, fecha_inicio, fecha_fin, precio_total, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, tuple(row))

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()

print(f"Datos importados correctamente desde {file_name} a la tabla '{table_name}' en '{db_path}'.")