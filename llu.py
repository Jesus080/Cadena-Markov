import numpy as np
import pandas as pd

# Definir los estados
states = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición (probabilidades de cambio de un estado a otro)
transition_matrix = pd.DataFrame({
    "Soleado": [0.7, 0.2, 0.1],  # Probabilidades desde el estado "Soleado"
    "Nublado": [0.3, 0.4, 0.3],  # Probabilidades desde el estado "Nublado"
    "Lluvioso": [0.2, 0.3, 0.5]   # Probabilidades desde el estado "Lluvioso"
}, index=states)

# Número de días a simular
num_days = 30

# Estado inicial
current_state = "Soleado"
weather_simulation = [current_state]

# Simulación de la cadena de Markov
for day in range(1, num_days):
    # Probabilidades de transición desde el estado actual
    probabilities = transition_matrix[current_state]
    
    # Elegir el siguiente estado según las probabilidades de transición
    next_state = np.random.choice(states, p=probabilities)
    
    # Guardar el estado
    weather_simulation.append(next_state)
    
    # Actualizar el estado actual
    current_state = next_state

# Crear un DataFrame con los resultados
weather_df = pd.DataFrame({
    "Día": np.arange(1, num_days+1),
    "Clima": weather_simulation
})

# Mostrar la simulación
print(weather_df)

# Contar cuántos días hubo de cada clima
weather_counts = weather_df["Clima"].value_counts()

print("\nConteo de días por tipo de clima:")
print(weather_counts)
