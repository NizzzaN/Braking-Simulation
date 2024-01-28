import matplotlib.pyplot as plt
import numpy as np


def simulate_motion(mass, velocity, road_type, wet_dry, inclination, sampling_time, max_simulation_time=300):
    g = 9.81 # Gravitational acceleration
    # Define the friction coefficients for different road types
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
        'water': {'dry': 0.08},
        'gravel': {'dry': 0.3},
        'sand': {'dry': 0.25}
    }

    # Select the appropriate friction coefficient based on the road type and conditions
    mu_static_selected = mu_static[road_type][wet_dry]
    mu_kinetic_selected = mu_kinetic[road_type][wet_dry]
    

    time = 0
    velocities = []
    distances = []
    total_distance = 0

    while velocity > 0 and time < max_simulation_time:
        time += sampling_time  # Move this line to the beginning of the loop

        # Use the kinetic friction coefficient while the vehicle is moving and the static one while it's stopping
        if velocity > 0:
            mu = mu_kinetic_selected
        else:
            mu = mu_static_selected

        force_friction = mu * mass * g * np.cos(np.arctan(inclination))
        force_acceleration = mass * g * np.sin(np.arctan(inclination))
        force_total = force_acceleration - force_friction

        acceleration = force_total / mass
        velocity += acceleration * sampling_time

        # Calculate distance travelled in this time step and add it to the total distance
        distance = velocity * sampling_time
        total_distance += distance

        velocities.append(velocity)
        distances.append(total_distance)

    return np.arange(0, time, sampling_time), velocities, distances

def plot_diagrams(time, velocities, distances, file_name_out):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(time, velocities, color ="green", lw = 2)
    plt.title('Velocity vs Time', fontweight ="bold")
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')

    plt.subplot(1, 2, 2)
    plt.plot(time, distances, color ="red", lw = 2)
    plt.title('Braking Distance vs Time', fontweight ="bold")
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')

    plt.tight_layout()
    plt.savefig(file_name_out)
    plt.show()
   
   
if __name__ == "__main__":
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter initial velocity (m/s): "))
    road_type = input("Enter road type (concrete, ice, water, gravel, sand): ")
    if road_type == 'water':
        wet_dry = 'aquaplaning'
    else:
        wet_dry = input("Enter road condition (dry, wet): ")
    
    inclination = float(input("Enter inclination (degrees): "))

    sampling_time = 0.1

    time, velocities, distances = simulate_motion(mass, velocity, road_type, wet_dry, inclination, sampling_time)
    plot_diagrams(time, velocities, distances, "BrakingTest.pdf")
  
    

  
   
