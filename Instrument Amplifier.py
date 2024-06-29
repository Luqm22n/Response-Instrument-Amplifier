import numpy as np
import matplotlib.pyplot as plt

def instrumentation_amplifier(V1, V2, R1, R2, R3, R4):
    # Menghitung tegangan diferensial pada amplifier instrumen
    Vd = (V2 - V1)

    # Menghitung tegangan keluaran amplifier instrumen
    Vo = (2 * Vd) * (R2 + R4) / (R1 * R3 + R1 * R4 + R2 * R3 + R2 * R4)

    return Vo

# Contoh penggunaan
V1 = 1.0  # Tegangan pada input non-inverting
V2 = 2.0  # Tegangan pada input inverting
R1 = 470.0  # Resistor pada input non-inverting
R2 = 1000.0  # Resistor pada input inverting
R3 = 1000.0  # Resistor pada feedback
R4 = 1000.0  # Resistor pada feedback

output_voltage = instrumentation_amplifier(V1, V2, R1, R2, R3, R4)

print(f"Tegangan Keluaran Amplifier Instrumentasi: {output_voltage} Volt")

# Membuat grafik respons amplifier terhadap perubahan tegangan pada input
V1_values = np.linspace(0, 5, 100)
V2_values = np.linspace(0, 5, 100)

output_values = np.zeros((len(V1_values), len(V2_values)))

for i, V1_val in enumerate(V1_values):
    for j, V2_val in enumerate(V2_values):
        output_values[i, j] = instrumentation_amplifier(V1_val, V2_val, R1, R2, R3, R4)

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
V1_mesh, V2_mesh = np.meshgrid(V1_values, V2_values)
ax.plot_surface(V1_mesh, V2_mesh, output_values.T, cmap='viridis')
ax.set_xlabel('Tegangan V1 (Volt)')
ax.set_ylabel('Tegangan V2 (Volt)')
ax.set_zlabel('Tegangan Keluaran (Volt)')
ax.set_title('Respon Amplifier Instrumentasi')
plt.show()
