import pandas as pd
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Cantidad de datos a generar
num_records = 100

# Generar datos aleatorios
data = {
"reserva_id": [i for i in range(1, num_records + 1)],  # IDs secuenciales
    "usuario_id": [i + num_records for i in range(1, num_records + 1)],  # IDs secuenciales a partir de un valor diferente
    "vehiculo_id": [i + 2 * num_records for i in range(1, num_records + 1)],  # IDs secuenciales a partir de un valor diferente
    "fecha_inicio": [fake.date_this_year() for _ in range(num_records)],
    "fecha_fin": [fake.date_this_year() for _ in range(num_records)],
    "precio_total": [round(random.uniform(100, 2000), 2) for _ in range(num_records)],
    "estado": [random.choice(["Pendiente", "Completado", "Cancelado"]) for _ in range(num_records)],
}

# Ajustar fechas de fin para que siempre sean después de la fecha de inicio
for i in range(num_records):
    if data["fecha_fin"][i] < data["fecha_inicio"][i]:
        data["fecha_fin"][i] = fake.date_between(start_date=data["fecha_inicio"][i])

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Exportar a Excel
file_name = "reservas_faker.xlsx"
df.to_excel(file_name, index=False)

# Ajustar el ancho de las columnas
from openpyxl import load_workbook

wb = load_workbook(file_name)
ws = wb.active

for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

wb.save(file_name)

print("Datos generados y exportados a reservas_faker.xlsx con ancho de columna ajustado")