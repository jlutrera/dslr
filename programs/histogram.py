import matplotlib.pyplot as plt
from . import *
from .utils import *

def normalize_grades(grades, a=-4, b=4):
	"""Normalize grades to a range of [-4, 4]"""
	min_grade = min(grades)
	max_grade = max(grades)

	normalized_grades = [(grade - min_grade) / (max_grade - min_grade) * (b - a) + a for grade in grades]
	return normalized_grades

def plot_normalized_histogram(data, houses):
	plt.figure(figsize=(10, 6))
	
	for house in houses:
		all_grades = []
		for subject, grades in data[house].items():
			normalized_grades = normalize_grades(grades)
			all_grades.extend(normalized_grades)
		plt.hist(all_grades, bins=20, alpha=0.35, label=house, edgecolor='black', linewidth=1.5)

	plt.title("Histogram of normalized grades by house")
	plt.xlabel("Normalized grades")
	plt.ylabel("Frecuency")
	plt.legend()
	plt.grid(True)
	plt.show()

def ask_for_houses(houses):
	while True:
		try:
			num_houses = int(input("How many houses do you want to show (0-4)? "))
			if 0 <= num_houses <= 4:
				break
			else:
				print(f"{RED}Error:{RESET} Invalid number. Please enter a number between 0 and 4.")
		except ValueError:
			print(f"{RED}Error:{RESET} Invalid number")

	if num_houses == 0:
		return [] 
	selected_houses = []
	if num_houses == 4:
		selected_houses = houses
		return selected_houses

	print(f"\n{YELLOW}Select the houses you want to show:{RESET}")
	for i, house in enumerate(houses, 1):
		print(f"  {YELLOW}{i}.{RESET} {house}")
	print()
	while len(selected_houses) < num_houses:
		try:
			selected = int(input(f"  Select a house (1-4): "))
			if 1 <= selected <= 4:
				house = houses[selected - 1]
				if house not in selected_houses:
					selected_houses.append(house)
					print(f"    {GREEN}{house}{RESET} selected.")
				else:
					print(f"    {RED}{house}{RESET} is already selected.")
			else:
				print(f"    {RED}Error:{RESET} Please, select a number between 1 and 4.")
		except ValueError:
			print(f"    {RED}Error:{RESET} Invalid number")

	return selected_houses

def histogram(data):
	houses = list(data.keys())
	selected_houses = ask_for_houses(houses)
	if selected_houses:
		plot_normalized_histogram(data, selected_houses)
		wait_for_keypress()
