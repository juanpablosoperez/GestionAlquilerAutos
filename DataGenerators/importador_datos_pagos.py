import pandas as pd
import sqlite3

# Nombre del archivo Excel generado
file_name = "pagos_faker.xlsx"

# Ruta al archivo de base de datos (está en el mismo directorio que el script)
db_path = '../Proyecto/gestion_alquiler_autos.db'

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(file_name)

# Convertir la columna de fecha a formato 'YYYY-MM-DD'
df['fecha_pago'] = pd.to_datetime(df['fecha_pago']).dt.strftime('%Y-%m-%d')

# Conectar a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Nombre de la tabla específica donde quieres insertar los datos
table_name = 'Pago'

# Verificar que la tabla existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
if cursor.fetchone() is None:
    print(f"La tabla '{table_name}' no existe en la base de datos.")
    conn.close()
    exit()

# Insertar los datos en la tabla específica
for i, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (pago_id, reserva_id, monto, fecha_pago)
        VALUES (?, ?, ?, ?)
    """, tuple(row))

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()

print(f"Datos importados correctamente desde {file_name} a la tabla '{table_name}' en '{db_path}'.")
