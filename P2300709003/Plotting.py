import matplotlib.pyplot as plt

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
