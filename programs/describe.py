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

def calc_statistics(data, house):
	statistics = {}
	features = data[house]

	for feature, values in features.items():
		if all(isinstance(x, (int, float)) for x in values) and values:
			# Ordenar los valores para calcular percentiles
			values.sort()

			count = len(values)
			mean = calc_mean(values)
			std = calc_std(values, mean)
			q0 = calc_percentile(values, 0)
			q1 = calc_percentile(values, 25)
			q2 = calc_percentile(values, 50)
			q3 = calc_percentile(values, 75)
			q4 = calc_percentile(values, 100)

			statistics[feature] = {
				'Count'	: count,
				'Mean'	: mean,
				'Std'	: std,
				'Min'	: q0,
				'Q1'	: q1,
				'Q2'	: q2,
				'Q3'	: q3,
				'Max'	: q4
			}

	return statistics

def print_table(statistics, max_feature_length=8):
	# Obtener las features (columnas) y los parámetros (filas)
	features = list(statistics.keys())
	truncated_features = [
		feature[:max_feature_length] + "…" if len(feature) > max_feature_length else feature
		for feature in features
	]
	params = ["Count", "Mean", "Std", "Min", "Q1", "Q2", "Q3", "Max"]

	# Determinar ancho de columna según el nombre más largo
	column_width = max(max_feature_length + 1, 10)  # Al menos 8 caracteres por columna

	# Imprimir encabezados
	print("".ljust(column_width), end="")
	for feature in truncated_features:
		print(f"{CYAN}{feature.ljust(column_width)}{RESET}", end="")
	print()

	# Imprimir filas con estadísticas
	for parameter in params:
		print(f"{CYAN}{parameter.ljust(column_width)}{RESET}", end="")
		for feature in features:
			value = statistics[feature][parameter]
			str_value = f"{value:.2f}" if isinstance(value, float) else str(value)
			print(str_value.ljust(column_width), end="")
		print()

def describe(data):
	selected_house = select_house(data)
	if not selected_house:
		return
	statistics = calc_statistics(data, selected_house)

	print(f"\n  {GREEN}Statistical Summary for House:{RESET} {selected_house}")
	if statistics:
		print_table(statistics)
	else:
		print(f"  {RED}Error: {RESET}No numerical features found for the selected house.")
