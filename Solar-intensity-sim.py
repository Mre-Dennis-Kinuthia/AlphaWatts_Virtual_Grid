#!/usr/bin/python3
import random

def simulate_solar_intensity(num_timesteps: int) -> list:
    """Simulates the solar intensity (W/m^2) over the course of a day.

    Parameters:
        num_timesteps: The number of time steps in the simulation.

    Returns:
        A list of solar intensity values for each time step.
    """
    # Generate random values for solar intensity (W/m^2)
    solar_intensity = []
    for i in range(num_timesteps):
        if i < num_timesteps / 2:  # Generate random values for first half of time steps
            solar_intensity.append(random.uniform(0, 1000))
        else:  # Set solar intensity to zero for second half of time steps
            solar_intensity.append(0)

    return solar_intensity

# Test the function
solar_intensity = simulate_solar_intensity(24)
print(solar_intensity)
