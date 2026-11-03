# Oscar Flores NC = 1389
import matplotlib.pyplot as plt
import numpy as np

Materias = ['MachineL','VisionA','LenguajeN','CienciasN','CienciasS']
Califas = [10, 9, 6, 8, 9]

plt.pie(Califas, labels=Materias, autopct= '%1.1f%%')
plt.title('Calificaciones-1389')
plt.show()
print("Programa realizado por Oscar Flores NC = 1389")