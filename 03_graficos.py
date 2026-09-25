import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("moviciudad_operaciones_limpio.csv")

columnas = [
    "tiempo_viaje_min",
    "retraso_min",
    "pasajeros_reportados"
]

for columna in columnas:
    df[columna] = pd.to_numeric(df[columna], errors="coerce")

plt.figure(figsize=(10, 5))
plt.hist(df["tiempo_viaje_min"].dropna(), bins=15)
plt.title("Distribución del tiempo de viaje")
plt.xlabel("Tiempo de viaje (minutos)")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.savefig("grafico_tiempo_viaje.png", dpi=300)
plt.show()

retrasos = df.groupby("ruta")["retraso_min"].mean()

plt.figure(figsize=(10, 5))
retrasos.plot(kind="bar")
plt.title("Promedio de retrasos por ruta")
plt.xlabel("Ruta")
plt.ylabel("Retraso promedio (minutos)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_retrasos_ruta.png", dpi=300)
plt.show()

pasajeros = df.groupby("ruta")["pasajeros_reportados"].mean()

plt.figure(figsize=(10, 5))
pasajeros.plot(kind="bar")
plt.title("Promedio de pasajeros por ruta")
plt.xlabel("Ruta")
plt.ylabel("Pasajeros promedio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_pasajeros_ruta.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["tiempo_viaje_min"], df["retraso_min"])
plt.title("Tiempo de viaje y retraso")
plt.xlabel("Tiempo de viaje (minutos)")
plt.ylabel("Retraso (minutos)")
plt.tight_layout()
plt.savefig("grafico_tiempo_retraso.png", dpi=300)
plt.show()

df.to_excel("moviciudad_operaciones_procesado.xlsx", index=False)

print("Proceso terminado correctamente.")
print("Gráficos y archivo Excel creados.")
