import matplotlib.pyplot as plt
from .utils import *


def normalize_values(values, target_min=-1000, target_max=1000):
    """Normaliza una lista de valores al rango especificado."""
    if not values:  # Si no hay valores, devolver una lista vacía
        return []
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:  # Si todos los valores son iguales, devolver el centro del rango
        return [0 for _ in values]
    return [((val - min_val) / (max_val - min_val)) * (target_max - target_min) + target_min for val in values]

def select_two_houses(data):
    """Permite al usuario seleccionar dos casas."""
    houses = list(data.keys())
    print("Houses available:")
    for i, house in enumerate(houses, 1):
        print(f"{i}. {house}")
    
    house1_idx = int(input("Select the first house (1 to 4): ")) - 1
    house2_idx = int(input("Select the second house (1 to 4, different from the first): ")) - 1
    
    if house1_idx == house2_idx:
        print("Error: Please select two different houses.")
        return select_two_houses(data)
    
    return houses[house1_idx], houses[house2_idx]

def select_common_features(data, house1, house2):
    """Permite al usuario seleccionar dos características comunes entre dos casas."""
    features1 = set(data[house1].keys())
    features2 = set(data[house2].keys())
    common_features = list(features1.intersection(features2))
    
    if not common_features:
        print("No common features available.")
        return None, None

    print("Common features available:")
    for i, feature in enumerate(common_features, 1):
        print(f"{i}. {feature}")
    
    feature1_idx = int(input("Select the first feature: ")) - 1
    feature2_idx = int(input("Select the second feature: ")) - 1
    
    feature1 = common_features[feature1_idx]
    feature2 = common_features[feature2_idx]
    
    return feature1, feature2

def scatter_plot(data):
    house1, house2 = select_two_houses(data)
    feature1, feature2 = select_common_features(data, house1, house2)

    """Genera un gráfico de dispersión entre dos casas para las mismas características."""
    values1_house1 = data[house1][feature1]
    values2_house1 = data[house1][feature2]
    values1_house2 = data[house2][feature1]
    values2_house2 = data[house2][feature2]

    # Hacer coincidir las longitudes de las listas para cada casa
    min_length1 = min(len(values1_house1), len(values2_house1))
    min_length2 = min(len(values1_house2), len(values2_house2))
    values1_house1 = values1_house1[:min_length1]
    values2_house1 = values2_house1[:min_length1]
    values1_house2 = values1_house2[:min_length2]
    values2_house2 = values2_house2[:min_length2]

    # Normalizar los valores
    norm_values1_house1 = normalize_values(values1_house1)
    norm_values2_house1 = normalize_values(values2_house1)
    norm_values1_house2 = normalize_values(values1_house2)
    norm_values2_house2 = normalize_values(values2_house2)

    # Graficar los datos
    plt.ion()
    plt.scatter(norm_values1_house1, norm_values2_house1, color='blue', alpha=0.7, label=house1)
    plt.scatter(norm_values1_house2, norm_values2_house2, color='orange', alpha=0.7, label=house2)
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.title(f"Scatter Plot")
    plt.legend()
    plt.grid(True)
    plt.get_current_fig_manager().canvas.manager.toolbar.pack_forget()
    plt.show()

    wait_for_keypress()