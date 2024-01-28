from Braking_Simulation import simulate_motion
from Plotting import plot_diagrams

if __name__ == "__main__":
    mass = float(input("Type mass (kg): "))
    velocity = float(input("Type initial velocity (m/s): "))
    road_type = input("Type road type (concrete, ice, water, gravel, sand): ")
    if road_type == 'water':
        wet_dry = 'aquaplaning'
    else:
        wet_dry = input("Enter road condition (dry, wet): ")
    inclination = float(input("Enter inclination (degrees): "))
    sampling_time = 0.1

    time, velocities, distances = simulate_motion(mass, velocity, road_type, wet_dry, inclination, sampling_time)
    
    # time, velocities, and distances need to have the same length
    min_length = min(len(time), len(velocities), len(distances))
    time = time[:min_length]
    velocities = velocities[:min_length]
    distances = distances[:min_length]
    #PLotting the results and saving the figure.
    plot_diagrams(time, velocities, distances, "P2300709003.pdf")
