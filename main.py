import pandas as pd
import re

# Leer el contenido del archivo
file_path = 'BL-Flickr-Images-Book.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    csv_content = file.read()

# Expresión regular para encontrar saltos de línea
line_pattern = re.compile(r'([^\n]*)(?:\n|$)')

# Expresión regular para dividir los campos de cada línea
csv_pattern = re.compile(r'(?:(?<=,)|(?<=^))"([^"]*(?:""[^"]*)*)"|([^,\n]+)|(?<=,)|(?<=\n)', re.MULTILINE)


rows = []

# Iterar sobre las líneas encontradas por la expresión regular
for match in line_pattern.finditer(csv_content):
    line = match.group(1)
    if line:  # Asegurarse de que la línea no esté vacía
        matches = csv_pattern.findall(line)
        row = [field[0] or field[1] for field in matches]
        rows.append(row)

# Crear un DataFrame a partir de las filas
df = pd.DataFrame(rows[1:], columns=rows[0])

print(df.head())
