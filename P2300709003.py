import matplotlib.pyplot as plt
import numpy as np

def simulate_motion(mass, velocity, road_type, wet_dry, inclination, sampling_time, max_simulation_time=300):
    g = 9.81

    # Define friction coefficients for different road types
    mu_static = {
        'concrete': {'dry': 0.65, 'wet': 0.4},
        'ice': {'dry': 0.2, 'wet': 0.1},
        'water': {'dry': 0.1},
        'gravel': {'dry': 0.35},
        'sand': {'dry': 0.3}
    }

    mu_kinetic = {
        'concrete': {'dry': 0.5, 'wet': 0.35},
        'ice': {'dry': 0.15, 'wet': 0.08},
        'water': {'dry': 0.05},
        'gravel': {'dry': 0.3},
        'sand': {'dry': 0.25}
    }

    # Select the appropriate friction coefficient based on the road type and conditions
    try:
        mu_static_selected = mu_static[road_type][wet_dry]
    except KeyError:
        mu_static_selected = mu_static[road_type]['dry']  # Use the 'dry' value if it doesn't exist your answer.

    try:
        mu_kinetic_selected = mu_kinetic[road_type][wet_dry]
    except KeyError:
        mu_kinetic_selected = mu_kinetic[road_type]['dry']   # Use the 'dry' value if it doesn't exist your answer.

    time = 0
    velocities = []
    distances = []
    total_distance = 0

    # Convert inclination from degrees to radians
    inclination = np.radians(inclination)

    while velocity > 0 and time < max_simulation_time:
        # Use kinetic friction when the vehicle is moving and the static one while it's stopping
        if velocity > 0:
            mu = mu_kinetic_selected
        else:
            mu = mu_static_selected

        force_friction = mu * mass * g * np.cos(inclination)
        force_acceleration = mass * g * np.sin(inclination)
        force_total = force_acceleration - force_friction

        acceleration = force_total / mass
        velocity += acceleration * sampling_time

        # If velocity becomes negative, set to zero and break the loop
        if velocity < 0:
            velocity = 0
            break

        # Calculate distance travelled in this time step and add it to the total distance
        distance = velocity * sampling_time
        total_distance += distance

        velocities.append(velocity)
        distances.append(total_distance)

        time += sampling_time  # Increase time

    return np.arange(0, time, sampling_time), velocities, distances

def plot_diagrams(time, velocities, distances,file_name_out):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(time, velocities, color ="green", lw = 2)
    plt.title('Velocity/time', fontweight ="bold")
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')

    plt.subplot(1, 2, 2)
    plt.plot(time, distances, color ="red", lw = 2)
    plt.title('Braking Distance', fontweight ="bold")
    plt.xlabel('Time (s)')
    plt.ylabel('Total Distance (m)')

    plt.tight_layout()
    plt.savefig(file_name_out)
    plt.show()


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
