import matplotlib.pyplot as plt

def normalize_grades(grades, a=-4, b=4):
    """Normaliza las notas a un rango [a, b] usando la normalización Min-Max."""
    min_grade = min(grades)
    max_grade = max(grades)
    
    # Aplicar la normalización
    normalized_grades = [
        (grade - min_grade) / (max_grade - min_grade) * (b - a) + a for grade in grades
    ]
    return normalized_grades

def histogram_quefunciona(data):
    """Dibuja el histograma de frecuencias de las notas normalizadas por casa."""
    houses = data.keys()
    plt.figure(figsize=(10, 6))
    
    for house in houses:
        all_grades = []
        for subject, grades in data[house].items():
            # Normalizar las notas para cada asignatura de la casa
            normalized_grades = normalize_grades(grades)
            all_grades.extend(normalized_grades)  # Unir todas las notas normalizadas
        
        # Dibujar el histograma con las notas normalizadas
        plt.hist(all_grades, bins=20, alpha=0.5, label=house,)
    
    plt.title("Distribución de notas normalizadas por casa")
    plt.xlabel("Notas normalizadas (rango [-4, 4])")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.grid(True)
    plt.show()

# Dibuja el histograma para las casas seleccionadas
def plot_normalized_histogram_of_grades(data, houses):
    plt.figure(figsize=(10, 6))
    
    for house in houses:
        all_grades = []
        for subject, grades in data[house].items():
            # Normalizar las notas para cada asignatura de la casa
            normalized_grades = normalize_grades(grades)
            all_grades.extend(normalized_grades)  # Unir todas las notas normalizadas
        
        # Dibujar el histograma con las notas normalizadas
        plt.hist(all_grades, bins=20, alpha=0.35, label=house, edgecolor='black', linewidth=1.5)
    plt.title("Histograma de distribución")
    plt.xlabel("Notas normalizadas")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para preguntar cuántas casas desea mostrar
def ask_for_houses_to_show(houses):
    while True:
        try:
            num_houses = int(input("¿Cuántas casas quieres mostrar? (1-4): "))
            if 1 <= num_houses <= 4:
                break
            else:
                print("Por favor, ingresa un número entre 1 y 4.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    selected_houses = []
    if num_houses == 4:
        selected_houses = houses
        return selected_houses

    print("\nSelecciona las casas para mostrar sus gráficos (usa los números 1-4):")
    for i, house in enumerate(houses, 1):
        print(f"{i}. {house}")

    while len(selected_houses) < num_houses:
        try:
            selected = int(input(f"\nSelecciona una casa (1-4): "))
            if 1 <= selected <= 4:
                house = houses[selected - 1]
                if house not in selected_houses:
                    selected_houses.append(house)
                    print(f"{house} seleccionada.")
                else:
                    print(f"{house} ya está seleccionada.")
            else:
                print("Por favor, selecciona un número entre 1 y 4.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    return selected_houses

# Función principal de ejecución del histograma
def histogram(data):
    # Listado de las casas disponibles
    houses = list(data.keys())
    
    # Preguntar cuántas casas se quieren mostrar y cuáles seleccionar
    selected_houses = ask_for_houses_to_show(houses)

    # Mostrar los gráficos para las casas seleccionadas
    print("\nMostrando los gráficos para las casas seleccionadas...")
    plot_normalized_histogram_of_grades(data, selected_houses)

