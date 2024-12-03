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

			count = max(num_data_by_subject)       
			mean = calc_mean(all_values)
			std = calc_std(all_values, mean)
			q0 = calc_percentile(all_values, 0)
			q1 = calc_percentile(all_values, 25)
			q2 = calc_percentile(all_values, 50)
			q3 = calc_percentile(all_values, 75)
			q4 = calc_percentile(all_values, 100)
			statistics[house] = {
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
	wait_for_keypress()
