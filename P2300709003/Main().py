# Main.py
import argparse
from Braking_Simulation import simulate_motion
from Plotting import plot_diagrams

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate motion.')
    parser.add_argument('--mass', type=float, required=True, help='Mass in kg')
    parser.add_argument('--velocity', type=float, required=True, help='Initial velocity in m/s')
    parser.add_argument('--road_type', type=str, required=True, help='Road type (concrete, ice, water, gravel, sand)')
    parser.add_argument('--wet_dry', type=str, required=False, help='Road condition (dry, wet)')
    parser.add_argument('--inclination', type=float, required=True, help='Inclination in degrees')
    parser.add_argument('--sampling_time', type=float, default=0.1, help='Sampling time')

    args = parser.parse_args()

    if args.road_type == 'water':
        args.wet_dry = 'aquaplaning'
    elif args.wet_dry is None and args.road_type != 'water':
        args.wet_dry = 'dry'

    time, velocities, distances = simulate_motion(args.mass, args.velocity, args.road_type, args.wet_dry, args.inclination, args.sampling_time)
    
    min_length = min(len(time), len(velocities), len(distances))
    time = time[:min_length]
    velocities = velocities[:min_length]
    distances = distances[:min_length]

    plot_diagrams(time, velocities, distances, "P2300709003.pdf")
