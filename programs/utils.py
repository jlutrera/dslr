from . import *

# Función para calcular la media
def calc_mean(values):
	return sum(values) / len(values) if values else None

# Función para calcular la desviación estándar
def calc_std(values, mean):
	n = len(values)
	var = sum((x - mean) ** 2 for x in values) / n
	std = var ** 0.5
	return std

def select_house(data):
	"""Permite al usuario seleccionar una casa."""
	houses = list(data.keys())
	print(f"  {GREEN}Available houses:{RESET}")
	for i, house in enumerate(houses, 1):
		print(f"    {i}. {house}")
	print(f"    {i + 1}. None")

	while True:
		house_idx = int(input(f"    {CYAN}Select one (1 to 4): {RESET}")) - 1
		if 0 <= house_idx <= len(houses) and int(house_idx) == house_idx:
			break
	if house_idx == len(houses):
		return None
	return houses[house_idx]

def select_features(data, house):
	"""Permite al usuario seleccionar características (features) de una casa."""
	features = list(data[house].keys())
	print(f"\n  {GREEN}Available features for {RESET}{house}:")
	for i, feature in enumerate(features, 1):
		print(f"    {i}. {feature}")
	print(f"    {i + 1}. None")

	while True:
		num_features = int(input(f"    {CYAN}How many features would you like to represent?{RESET} "))
		if 0 <= num_features <= len(features) and int(num_features) == num_features:
			break
	if num_features == 0:
		return None
	selected_features = []

	for _ in range(num_features):
		while True:
			feature_idx = int(input(f"    {CYAN}Select a feature (1 to {len(features)+1}): {RESET}")) - 1
			if 0 <= feature_idx <= len(features) and int(feature_idx) == feature_idx:
				break
		if feature_idx != len(features):
			selected_features.append(features[feature_idx])

	return selected_features

def normalize_values(values, new_min=-4, new_max=4):
	"""Normaliza una lista de valores al rango [new_min, new_max]."""
	old_min, old_max = min(values), max(values)
	if old_max - old_min == 0:
		return [0] * len(values)  # Evita división por cero si todos los valores son iguales
	return [
		new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)
		for value in values
	]

__all__ = [
	'calc_mean',
	'calc_std',
	'select_house',
	'select_features',
	'normalize_values'
	]
