import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from . import *
from .utils import *

# Función para calcular el coeficiente de variación
def calc_cv(values):
	"""Calcula el coeficiente de variación para una lista de valores."""
	mean = calc_mean(values)
	std = calc_std(values, mean)
	if mean != 0:
		return std / mean
	return float('inf')
             
def find_top_homogeneous_feature(data):
	"""Encuentra las 10 features más homogéneas considerando todas las casas."""
	cv_values = []

	for house, features in data.items():
		for feature, values in features.items():
			if values:
				cv = calc_cv(values)
				cv_values.append((house, feature, cv))

	# Ordenar por CV de menor a mayor (más homogéneo primero)
	cv_values.sort(key=lambda x: x[2])

	# Imprimir las 10 features más homogéneas
	top_ten = cv_values[:10]
	print(f"  {GREEN}Most homogeneous features:{RESET}")
	print(f"    {CYAN}{'Rank':<5} {'House':<15} {'Feature':<30} {'CV':<10}{RESET}")
	for rank, (house, feature, cv) in enumerate(top_ten, start=1):
		print(f"    {rank:<5} {house:<15} {feature:<30} {cv:.4f}")
	print()

	# Devolver el primero
	return top_ten[0]
    
def histogram(data):
	# Calcular la feature más homogénea
	most_homogeneous_house, most_homogeneous_feature, _ = find_top_homogeneous_feature(data)
	homogeneous_values = data[most_homogeneous_house][most_homogeneous_feature]
	normalized_homogeneous_values = normalize_values(homogeneous_values)
	
	message_title = "Histogram: Most Homogeneous"
	# Seleccionar casa y features
	house = select_house(data)
	if house:
		features = select_features(data, house)
		# Histograma de la feature más homogénea
		# Crear gráfico
		plt.ion()
		plt.figure(figsize=(10, 7))
		manager = plt.get_current_fig_manager()
		manager.set_window_title('Histogram')
		plt.hist(normalized_homogeneous_values, bins=20, edgecolor='black', alpha=0.7, color='blue',
			density=True, label=f"{most_homogeneous_feature} ({most_homogeneous_house})")
		if features:
			# Histogramas de las features seleccionadas
			for feature in features:
				values = data[house][feature]
				if not values:
					continue
				normalized_values = normalize_values(values)
				plt.hist(normalized_values, bins=20, edgecolor='black', alpha=0.5, 
					density=True, label=f"{feature} ({house})")
			message_title += " & Selection" 
	else:
		plt.ion()
		plt.figure(figsize=(10, 7))
		manager = plt.get_current_fig_manager()
		manager.set_window_title('Histogram')
		plt.hist(normalized_homogeneous_values, bins=20, edgecolor='black', alpha=0.7, color='blue',
			density=True, label=f"{most_homogeneous_feature} ({most_homogeneous_house})")
	# Configurar gráfico
	plt.title(message_title)
	plt.xlabel('Values (Normalized)')
	plt.ylabel('Frequency (Normalized)')
	plt.legend(loc='upper right')
	plt.tight_layout()

	# Quito la barra de herramientas
	plt.get_current_fig_manager().canvas.manager.toolbar.pack_forget()

	plt.show()
