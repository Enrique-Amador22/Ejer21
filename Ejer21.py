import pandas as pd
import re

df = pd.read_csv("carpetasFGJ_acumulado_2024_09.csv", delimiter=",", low_memory=False)

print(df.head())

print("\nNumero de valores no vacios en 'delito':", df["delito"].count())
print("Numero de valores unicos en 'delito':", df["delito"].nunique())

df_robo_negocio = df[df["delito"].str.upper().str.contains("ROBO A NEGOCIO", na=False)]
df_robo_evento = df[df["delito"].str.upper().str.contains("ROBO EN EVENTO", na=False)]

print("\n=== Estadisticas sobre 'ROBO A NEGOCIO' y 'ROBO EN UN EVENTO' ===")
print("Total de registros en el CSV:         ", len(df))
print("Registros con 'ROBO A NEGOCIO':        ", len(df_robo_negocio))
print("Registros con 'ROBO EN UN EVENTO':        ", len(df_robo_evento))

print("\n=== Ejemplos de delitos de ROBO A NEGOCIO ===")
print(df_robo_negocio["delito"].head(5))

print("\n=== Ejemplos de delitos de ROBO EN UN EVENTO ===")
print(df_robo_evento["delito"].head(5))


