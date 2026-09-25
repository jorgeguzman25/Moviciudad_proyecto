import pandas as pd

df = pd.read_csv("moviciudad_operaciones_limpio.csv")

columnas = [
    "tiempo_viaje_min",
    "retraso_min",
    "pasajeros_reportados"
]

for columna in columnas:
    df[columna] = pd.to_numeric(df[columna], errors="coerce")

print("================================")
print("ESTADÍSTICA DESCRIPTIVA")
print("================================")
print(df[columnas].describe())

print("\n================================")
print("VALORES ATÍPICOS")
print("================================")

for columna in columnas:
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    atipicos = df[
        (df[columna] < limite_inferior) |
        (df[columna] > limite_superior)
    ]

    print("\nVariable:", columna)
    print("Cantidad de valores atípicos:", len(atipicos))

print("\n================================")
print("MATRIZ DE CORRELACIONES")
print("================================")

correlaciones = df[columnas].corr()
print(correlaciones)

correlaciones.to_csv(
    "correlaciones_moviciudad.csv",
    encoding="utf-8-sig"
)

print("\nAnálisis estadístico terminado.")
