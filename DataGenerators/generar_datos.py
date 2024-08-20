import pandas as pd
from faker import Faker
from openpyxl import load_workbook

# Inicializar Faker
fake = Faker()

# Cantidad de datos a generar
num_records = 100

# Generar datos aleatorios
data = {
    "Nombre": [fake.first_name() for _ in range(num_records)],
    "Apellido": [fake.last_name() for _ in range(num_records)],
    "Correo Electrónico": [fake.email() for _ in range(num_records)],
    "Teléfono": [fake.phone_number() for _ in range(num_records)],
    "Dirección": [fake.address() for _ in range(num_records)],
    "Fecha de Nacimiento": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_records)],
    "Empresa": [fake.company() for _ in range(num_records)],
    "País": [fake.country() for _ in range(num_records)],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Exportar a Excel
file_name = "datos_faker.xlsx"
df.to_excel(file_name, index=False)

# Ajustar el ancho de las columnas
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

print("Datos generados y exportados a datos_faker.xlsx con ancho de columna ajustado")