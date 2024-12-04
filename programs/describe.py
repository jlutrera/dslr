# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 20:36:42 by jutrera-          #+#    #+#              #
#    Updated: 2024/12/02 20:36:42 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from . import *
from .utils import *

def calc_percentile(values, percentile):
	if percentile == 0:
		return values[0]
	if percentile == 100:
		return values[-1]
	
	n = len(values)
	index = (n + 1) * percentile / 100
	if index.is_integer():
		return values[int(index) - 1]
	else:
		floor_index = int(index)
		f = index - floor_index
		return values[floor_index - 1] + f * (values[floor_index] - values[floor_index - 1])

def calc_std(values, mean):
	n = len(values)
	var = sum((x - mean) ** 2 for x in values) / n
	std = var ** 0.5
	return std

def calc_mean(values):
	return sum(values) / len(values)

def calc_statistics(data):
	statistics = {}

	# Iterar por todas las asignaturas
	for feature in next(iter(data.values())).keys():  # Usa las claves de cualquier casa como referencia
		all_values = []

		# Reunir los valores de todas las casas para la asignatura actual
		for house in data:
			all_values.extend(data[house][feature])

		if all_values:
			# Ordenar los valores para calcular percentiles
			all_values.sort()

			count = len(all_values)
			mean = calc_mean(all_values)
			std = calc_std(all_values, mean)
			q0 = calc_percentile(all_values, 0)
			q1 = calc_percentile(all_values, 25)
			q2 = calc_percentile(all_values, 50)
			q3 = calc_percentile(all_values, 75)
			q4 = calc_percentile(all_values, 100)

			statistics[feature] = {
				'Count' : count,
				'Mean'  : mean,
				'Std'   : std,
				'Min'   : q0,
				'Q1'    : q1,
				'Q2'    : q2,
				'Q3'    : q3,
				'Max'   : q4
			}

	return statistics

def print_table(statistics, max_feature_length=8):
	"""
	Imprime una tabla con nombres de features truncados a un número fijo de caracteres.
	Args:
		statistics (dict): Estadísticas calculadas.
		max_feature_length (int): Máximo número de caracteres para los nombres de las features.
	"""
	# Obtener las features (columnas) y los parámetros (filas)
	features = list(statistics.keys())
	truncated_features = [
		feature[:max_feature_length] + "…" if len(feature) > max_feature_length else feature 
		for feature in features
	]
	params = ["Count", "Mean", "Std", "Min", "Q1", "Q2", "Q3", "Max"]

	# Determinar ancho de columna según el nombre más largo
	column_width = max(max_feature_length + 1, 12)  # Al menos 8 caracteres por columna

	# Imprimir encabezados
	print("".ljust(column_width), end="")
	for feature in truncated_features:
		print(f"{YELLOW}{feature.ljust(column_width)}{RESET}", end="")
	print()

	# Imprimir filas con estadísticas
	for parameter in params:
		print(f"{YELLOW}{parameter.ljust(column_width)}{RESET}", end="")
		for feature in features:
			value = statistics[feature][parameter]
			str_value = f"{value:.2f}" if isinstance(value, float) else str(value)
			print(str_value.ljust(column_width), end="")
		print()

def describe(data):
	statistics = calc_statistics(data)
	print_table(statistics)
	wait_for_keypress()
