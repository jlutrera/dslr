import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from . import *

def normalize_values(values, new_min=-4, new_max=4):
	"""Normaliza una lista de valores al rango [new_min, new_max]."""
	old_min, old_max = min(values), max(values)
	if old_max - old_min == 0:
		return [0] * len(values)  # Evita división por cero si todos los valores son iguales
	return [
		new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)
		for value in values
	]

# Función para calcular la media
def calc_mean(values):
	"""Calcula la media de una lista de valores."""
	return sum(values) / len(values) if values else 0

# Función para calcular la desviación estándar
def calc_std(values, mean):
	"""Calcula la desviación estándar de una lista de valores."""
	return (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5 if values else 0

# Función para calcular el coeficiente de variación
def calc_cv(values):
	"""Calcula el coeficiente de variación para una lista de valores."""
	mean = calc_mean(values)
	std = calc_std(values, mean)
	if mean != 0:
		return std / mean
	return float('inf')

def find_most_homogeneous_features(data):
	cv_results = []

	for house, subjects in data.items():
		for feature, values in subjects.items():
			if values:
				cv = calc_cv(values)
				cv_results.append((cv, house, feature))

	# Ordenamos las *features* por su coeficiente de variación en orden ascendente
	cv_results.sort()

	# Extraemos las 10 *features* más homogéneas
	most_homogeneous = cv_results[:10]
	return most_homogeneous

def print_most_homogeneous(features_list):
	print(f"  {GREEN}Most homogeneous features:{RESET}")
	print(f"    {CYAN}{'Rank':<5} {'House':<15} {'Feature':<30} {'CV':<10}{RESET}")
	for rank, (house, feature, cv) in enumerate(features_list, start=1):
		print(f"    {rank:<5} {house:<15} {feature:<30} {cv:.4f}")
        
def select_house(data):
	"""Permite al usuario seleccionar una casa."""
	houses = list(data.keys())
	print(f"\n  {GREEN}Houses available:{RESET}")
	for i, house in enumerate(houses, 1):
		print(f"    {i}. {house}")

	house_idx = int(input(f"    {CYAN}Select a house (1 to 4): {RESET}")) - 1
	return houses[house_idx]
     
def select_features(data, house):
	"""Permite al usuario seleccionar características (features) de una casa."""
	features = list(data[house].keys())
	print(f"\n  {GREEN}Available features for {RESET}{house}:")
	for i, feature in enumerate(features, 1):
		print(f"    {i}. {feature}")

	num_features = int(input(f"    {CYAN}How many features would you like to represent?{RESET} "))
	selected_features = []

	for _ in range(num_features):
		feature_idx = int(input(f"    {CYAN}Select a feature (1 to {len(features)}): {RESET}")) - 1
		selected_features.append(features[feature_idx])

	return selected_features

def find_top_homogeneous_features(data):
	"""Encuentra las 10 features más homogéneas considerando todas las casas."""
	cv_values = []

	for house, features in data.items():
		for feature, values in features.items():
			if values:
				cv = calc_cv(values)
				cv_values.append((house, feature, cv))

	# Ordenar por CV de menor a mayor (más homogéneo primero)
	cv_values.sort(key=lambda x: x[2])
	# Devolver las 10 más homogéneas
	return cv_values[:10]
    
def histogram(data):
	# Calcular la feature más homogénea
	top_features = find_top_homogeneous_features(data)
	most_homogeneous_house, most_homogeneous_feature, _ = top_features[0]
	homogeneous_values = data[most_homogeneous_house][most_homogeneous_feature]
	normalized_homogeneous_values = normalize_values(homogeneous_values)

	# Mostrar las 10 features más homogéneas
	print_most_homogeneous(top_features)

	# Seleccionar casa y features
	house = select_house(data)
	features = select_features(data, house)

	# Crear gráfico
	plt.ion()
	plt.figure(figsize=(10, 7))

	# Histograma de la feature más homogénea
	plt.hist(normalized_homogeneous_values, bins=20, edgecolor='black', alpha=0.7, color='blue',
		density=True, label=f"{most_homogeneous_feature} (House: {most_homogeneous_house})")

	# Histogramas de las features seleccionadas
	for feature in features:
		values = data[house][feature]
		if not values:
			continue
		normalized_values = normalize_values(values)
		plt.hist(normalized_values, bins=20, edgecolor='black', alpha=0.5, density=True, label=feature)

	# Configurar gráfico
	plt.title("Histograms: Most Homogeneous & Selected Features")
	plt.xlabel('Values (Normalized)')
	plt.ylabel('Frequency (Normalized)')
	plt.legend(loc='upper right')
	plt.tight_layout()

	# Quito la barra de herramientas
	plt.get_current_fig_manager().canvas.manager.toolbar.pack_forget()

	plt.show()
