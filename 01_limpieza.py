import pandas as pd

df = pd.read_csv("moviciudad_operaciones_bruto_SET_A.csv")

print("Datos originales:")
print(df.head())
print("\nCantidad de registros:", len(df))

df.columns = df.columns.str.strip()

for columna in df.select_dtypes(include="object").columns:
    df[columna] = df[columna].str.strip()

df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")

columnas_numericas = [
    "tiempo_viaje_min",
    "retraso_min",
    "pasajeros_reportados"
]

for columna in columnas_numericas:
    df[columna] = pd.to_numeric(df[columna], errors="coerce")

print("\nDatos faltantes:")
print(df.isnull().sum())

print("\nDuplicados encontrados:", df.duplicated().sum())
df = df.drop_duplicates()

df = df.sort_values("fecha_registro")
df = df.reset_index(drop=True)

df.to_csv(
    "moviciudad_operaciones_limpio.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nLimpieza terminada.")
print("Registros finales:", len(df))
print("Archivo creado: moviciudad_operaciones_limpio.csv")
