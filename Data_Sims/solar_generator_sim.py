#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
.. module:: __init__
    :synopsis: the top-level module of TcEx Utils.
"""

import random
from solar_intensity_sim import simulate_solar_intensity


def simulate_energy_generation(num_timesteps: int, solar_farm_size: float, panel_efficiency: float, sunlight_threshold: float) -> list:
    """Simulates the solar energy generation (kWh) over the course of a day.

    Parameters:
        num_timesteps: The number of time steps in the simulation.
        solar_farm_size: The size of the solar farm in acres.
        panel_efficiency: The efficiency of the solar panels.
        sunlight_threshold: The minimum solar intensity (W/m^2) for energy generation.

    Returns:
        A list of solar energy generation values for each time step.
    """
    # Generate random values for solar intensity (W/m^2)
    solar_intensity = simulate_solar_intensity(num_timesteps)

    # Calculate energy generation (kWh) for each time step
    energy_generation = []
    for intensity in solar_intensity:
        if intensity > sunlight_threshold:
            energy_generation.append(solar_farm_size * panel_efficiency * intensity)
        else:
            energy_generation.append(0)

    return energy_generation

# Test the function
energy_generation = simulate_energy_generation(24, 1, 0.2, 50)

# Print the energy generation for each time step
for i, gen in enumerate(energy_generation):
    print(f"Time step {i}: {gen:.2f} kWh")
