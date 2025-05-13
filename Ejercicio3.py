import numpy as np
import matplotlib.pyplot as plt

# Datos de altitud (km) y consumo (kg/h)
x_points = np.array([2.0, 4.0, 6.0, 8.0])
y_points = np.array([2500, 2300, 2150, 2050])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Estimar el consumo a una altitud de 5 km
x_target = 5.0
y_target = lagrange_interpolation(x_target, x_points, y_points)
print(f"El consumo estimado a una altitud de {x_target} km es {y_target:.2f} kg/h")

# Generar datos para graficar la interpolación
x_values = np.linspace(min(x_points), max(x_points), 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los datos originales y la interpolación
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales")
plt.axvline(x=x_target, color="green", linestyle="--", label=f"Altitud estimada (x = {x_target} km)")
plt.scatter([x_target], [y_target], color="purple", label=f"Consumo estimado ({y_target:.2f} kg/h)")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.title("Consumo de Combustible - Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("consumo_combustible.png")
plt.show()
