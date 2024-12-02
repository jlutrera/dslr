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

def calc_percentile(values, percentile):
	k = (len(values) - 1) * percentile / 100
	i = int(k)
	f = k - i
	if i + 1 < len(values):
		return values[i] * (1 - f) + values[i + 1] * f
	else:
		return values[i]
                
def calc_statistics(data):
	statistics = {}
	for house, subjects in data.items():
		all_values = []
		num_data_by_subject = []

		for values in subjects.values():
			if values:
				all_values.extend(values)
				num_data_by_subject.append(len(values))

		if all_values:
			# Sorted values to calculate percentiles
			all_values.sort()
			n = len(all_values)

			count = max(num_data_by_subject)       
			total_add = sum(all_values)
			mean = total_add / n
			var = sum((x - mean) ** 2 for x in all_values) / n
			std = var ** 0.5
			min_value = all_values[0]
			max_value = all_values[-1]
			q1 = calc_percentile(all_values, 25)
			q2 = calc_percentile(all_values, 50)
			q3 = calc_percentile(all_values, 75)

			statistics[house] = {
				'Count'	: count,
				'Mean'	: mean,
				'Std'	: std,
				'Min'	: min_value,
				'Q1'	: q1,
				'Q2'	: q2,
				'Q3'	: q3,
				'Max'	: max_value
			} 
	return statistics

def print_table(statistics):
	# Get houses and parameters(columns)
	houses = list(statistics.keys())
	params = ["Count", "Mean", "Std", "Min", "Q1", "Q2", "Q3", "Max"]

	print("\t", end="")
	for house in houses:
		print(f"{YELLOW}{house}{RESET}\t", end="")
	print()
	# Build and print rows
	for parameter in params:
		print(f"{YELLOW}{parameter}{RESET}", end="\t")
		for house in houses:
			value = statistics[house][parameter]
			str_value = f"{value:.2f}" if isinstance(value, float) else str(value)
			print(str_value+"\t", end="")
			if len(str_value) < 8:
				print("\t", end="")
		print()

def describe(data):
	statistics = calc_statistics(data)
	print_table(statistics)
