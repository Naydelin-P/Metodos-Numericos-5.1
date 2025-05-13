#   Código que implementa la interpolación de Lagrange
#   para ajustar un conjunto de datos
#
#  Naydelin Palomo Martinez

import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
x_points = np.array([0.5, 1, 1.5, 2])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

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

# Evaluar la interpolación en un valor específico
x_target = 1.25
y_target = lagrange_interpolation(x_target, x_points, y_points)
print(f"La deformación esperada en x = {x_target} es y = {y_target:.2f}")

# Puntos para graficar la interpolación
x_values = np.linspace(min(x_points), max(x_points), 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(6,4))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Puntos dados")
plt.axvline(x=x_target, color="green", linestyle="--", label=f"x = {x_target}")
plt.scatter([x_target], [y_target], color="purple", label=f"Punto interpolado (x={x_target}, y={y_target:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("lagrange_interpolacion.png")
plt.show()
