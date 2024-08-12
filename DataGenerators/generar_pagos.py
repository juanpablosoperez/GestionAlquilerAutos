import pandas as pd
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Cantidad de datos a generar
num_records = 100

# Generar datos aleatorios
data = {
    "pago_id": list(range(1, num_records + 1)),
    "reserva_id": list(range(1, num_records + 1)),
    "monto": [round(random.uniform(50, 1000), 2) for _ in range(num_records)],
    "fecha_pago": [fake.date_this_year() for _ in range(num_records)],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Exportar a Excel
file_name = "pagos_faker.xlsx"
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

print("Datos generados y exportados a pagos_faker.xlsx con ancho de columna ajustado")