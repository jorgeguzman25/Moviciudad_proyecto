import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("moviciudad_operaciones_limpio.csv")

columnas = [
    "tiempo_viaje_min",
    "retraso_min",
    "pasajeros_reportados"
]

for columna in columnas:
    df[columna] = pd.to_numeric(df[columna], errors="coerce")

df = df.dropna(subset=columnas)

X = df[["retraso_min", "pasajeros_reportados"]]
y = df["tiempo_viaje_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

mae = mean_absolute_error(y_test, predicciones)
mse = mean_squared_error(y_test, predicciones)

print("================================")
print("RESULTADOS DEL MODELO")
print("================================")
print("MAE:", mae)
print("MSE:", mse)

resultados = pd.DataFrame({
    "Tiempo_real": y_test.values,
    "Tiempo_estimado": predicciones
})

print("\nComparación:")
print(resultados.head(10))

resultados.to_csv(
    "resultados_regresion.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArchivo resultados_regresion.csv creado.")
