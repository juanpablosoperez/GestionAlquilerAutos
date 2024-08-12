import pandas as pd
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Cantidad de datos a generar
num_records = 100

# Opciones para marca, modelo, y tipo de vehículo
marcas = ["Toyota", "Ford", "Chevrolet", "Honda", "Nissan"]
modelos = ["Corolla", "Fiesta", "Civic", "Accord", "Altima", "Cruze", "Camaro"]
colores = ["Rojo", "Azul", "Negro", "Blanco", "Gris", "Verde"]
tipos = ["Sedan", "SUV", "Camioneta", "Hatchback", "Convertible"]

# Generar datos aleatorios
data = {
    "vehiculo_id": list(range(1, num_records + 1)),
    "marca": [random.choice(marcas) for _ in range(num_records)],
    "modelo": [random.choice(modelos) for _ in range(num_records)],
    "anio": [random.randint(2000, 2023) for _ in range(num_records)],
    "precio_por_dia": [round(random.uniform(30, 150), 2) for _ in range(num_records)],
    "disponibilidad": [random.choice([True, False]) for _ in range(num_records)],
    "matricula": [fake.license_plate() for _ in range(num_records)],
    "color": [random.choice(colores) for _ in range(num_records)],
    "tipo": [random.choice(tipos) for _ in range(num_records)],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Exportar a Excel
file_name = "vehiculos_faker.xlsx"
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

print("Datos generados y exportados a vehiculos_faker.xlsx con ancho de columna ajustado")