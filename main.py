
from programs import *
from programs.describe import describe
from programs.histogram import histogram
from programs.scatter_plot import scatter_plot
from programs.pair_plot import pair_plot
from programs.logreg_predict import logreg_predict
from programs.logreg_train import logreg_train
from programs.utils import *
import sys, csv, os
from collections import defaultdict

def clear_terminal():
	# Para Linux y macOS
	if os.name == 'posix':
		os.system('clear')
	# Para Windows
	elif os.name == 'nt':
		os.system('cls')

def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

def print_menu():
	#clear_terminal()
	print()
	print(f"{YELLOW}Available programs:{RESET}\n")
	print(f"  {YELLOW}1.{RESET} Statistics")
	print(f"  {YELLOW}2.{RESET} Histogram")
	print(f"  {YELLOW}3.{RESET} Scatter plot")
	print(f"  {YELLOW}4.{RESET} Pair plot")
	print(f"  {YELLOW}5.{RESET} Train the model and predict")
	print(f"  {YELLOW}6.{RESET} Exit")
	print()
	option = input(f"  Select an option: {YELLOW}")
	print(f"{RESET}")

	return option

def read_csv_data(filename):
    data = defaultdict(lambda: defaultdict(list))
    filename = "datasets/" + filename
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            house = row['Hogwarts House']
            for subject, value in row.items():
                if subject not in {'Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'}:
                    if value:
                        try:
                            data[house][subject].append(float(value))
                        except ValueError:
                            pass
    return data

def main():
	if len(sys.argv) != 2:
		print(f"{RED}Error:{RESET} Type \"python3 main.py <archivo.csv>\"")
		return
	data = read_csv_data(sys.argv[1])
	if data is None:
		return
	
	while True:
		option = print_menu()
		if option == "1":
			describe(data)
		elif option == "2":
			histogram(data)
		elif option == "3":
			scatter_plot(data)
		elif option == "4":
			pair_plot(data)
		elif option == "5":
			logreg_train(data)
			logreg_predict()
		elif option == "6":
			break
		else:
			print(f"{RED}Error: {RESET}Invalid option. Try again.")
			wait_for_keypress()
	print("BYE!")

if __name__ == "__main__":
    main()
