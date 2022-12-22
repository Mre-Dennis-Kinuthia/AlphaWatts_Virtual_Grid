#!/usr/bin/python3

import random

# Constants
NUM_TIMESTEPS = 24  # Number of time steps in a day
SOLAR_FARM_SIZE = 1  # Size of solar farm in acres
PANEL_EFFICIENCY = 0.2  # Efficiency of solar panels
SUNLIGHT_THRESHOLD = 1  # Minimum solar intensity (W/m^2) for energy generation

# Generate random values for solar intensity (W/m^2)
solar_intensity = [random.uniform(0, 1000) for _ in range(NUM_TIMESTEPS)]

# Calculate energy generation (kWh) for each time step
energy_generation = []
for intensity in solar_intensity:
    if intensity > SUNLIGHT_THRESHOLD:
        energy_generation.append(SOLAR_FARM_SIZE * PANEL_EFFICIENCY * intensity)
    else:
        energy_generation.append(0)

# Print the energy generation for each time step
for i, gen in enumerate(energy_generation):
    print(f"Time step {i}: {gen:.2f} kWh")
