
import sys
import matplotlib.pyplot as plt

def normalize_data(values, new_min=0, new_max=1000):
    """Normaliza los datos al rango [new_min, new_max] utilizando Min-Max scaling."""
    if not values:
        return []

    old_min, old_max = min(values), max(values)
    if old_min == old_max:
        return [new_min + (new_max - new_min) / 2] * len(values)  # Todos los valores iguales.

    return [
        new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)
        for value in values
    ]

def plot_scatter(house_data, house1, house2):
    """Dibuja un gráfico de dispersión comparando las dos casas seleccionadas."""
    scores_house1 = house_data[house1]
    scores_house2 = house_data[house2]

    # Asegurarse de que ambas listas tengan la misma longitud
    common_scores = list(zip(scores_house1, scores_house2))
    
    # Eliminar pares donde uno de los valores esté vacío (NaN)
    common_scores = [pair for pair in common_scores if None not in pair]

    # Separar las puntuaciones después de la limpieza
    scores_house1 = [pair[0] for pair in common_scores]
    scores_house2 = [pair[1] for pair in common_scores]

    # Normalización de las puntuaciones
    normalized_house1 = normalize_data(scores_house1, new_min=0, new_max=1000)
    normalized_house2 = normalize_data(scores_house2, new_min=0, new_max=1000)

    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 6))

    # Graficar los puntos de cada casa
    plt.scatter(normalized_house1, normalized_house2, alpha=0.5, color="purple", edgecolors="black")

    # Personalización del gráfico
    plt.title(f"Comparación de Notas Normalizadas: {house1} vs {house2}", fontsize=16)
    plt.xlabel(f"Puntuaciones Normalizadas de {house1}", fontsize=14)
    plt.ylabel(f"Puntuaciones Normalizadas de {house2}", fontsize=14)
    plt.grid(True, axis="both", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

def scatter_plot(data):
    # Mostrar el menú para seleccionar dos casas
    print("Selecciona dos casas de Hogwarts para comparar:")
    print("1. Gryffindor")
    print("2. Hufflepuff")
    print("3. Ravenclaw")
    print("4. Slytherin")
    
    # Solicitar la primera casa
    house1_choice = int(input("Selecciona la primera casa (1-4): "))
    house1_map = {1: "Gryffindor", 2: "Hufflepuff", 3: "Ravenclaw", 4: "Slytherin"}
    house1 = house1_map.get(house1_choice)

    # Solicitar la segunda casa
    house2_choice = int(input("Selecciona la segunda casa (1-4): "))
    house2_map = {1: "Gryffindor", 2: "Hufflepuff", 3: "Ravenclaw", 4: "Slytherin"}
    house2 = house2_map.get(house2_choice)

    # Verificar que ambas casas son válidas
    if house1 not in data or house2 not in data:
        print("Una o ambas casas no existen en los datos. Intenta nuevamente.")
        sys.exit(1)

    # Mostrar el gráfico comparando las dos casas
    plot_scatter(data, house1, house2)
