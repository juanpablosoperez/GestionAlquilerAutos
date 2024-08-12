import pandas as pd
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Cantidad de datos a generar
num_records = 100

# Generar datos aleatorios
data = {
    "usuario_id": list(range(1, num_records + 1)),
    "nombre": [fake.first_name() for _ in range(num_records)],
    "apellido": [fake.last_name() for _ in range(num_records)],
    "email": [fake.email() for _ in range(num_records)],
    "password": [fake.password(length=10) for _ in range(num_records)],
    "telefono": [fake.phone_number() for _ in range(num_records)],
    "direccion": [fake.address() for _ in range(num_records)],
    "tipo": [random.choice(["administrador", "cliente"]) for _ in range(num_records)]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Exportar a Excel
file_name = "usuarios_faker.xlsx"
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

print("Datos generados y exportados a usuarios_faker.xlsx con ancho de columna ajustado")