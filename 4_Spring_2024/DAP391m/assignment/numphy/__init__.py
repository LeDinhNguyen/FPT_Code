import numpy as np


def draw_circle(center_lat, center_lon, elevation):
    earth_radius = 6371000
    num_points = 10

    circle_points = []
    for i in range(0, 360 + 360 // num_points, 360 // num_points):
        angle = np.deg2rad(i)
        delta_lat = (np.sqrt(1000**2 - elevation**2) / earth_radius) * np.cos(angle)
        delta_lon = (np.sqrt(1000**2 - elevation**2) / earth_radius) * np.sin(angle) / np.cos(np.radians(center_lat))
        
        lat = center_lat + np.degrees(delta_lat)
        lon = center_lon + np.degrees(delta_lon)
        circle_points.append((lat, lon))

    # Extract latitude and longitude arrays for plotting
    circle_latitudes, circle_longitudes = zip(*circle_points)
    return circle_latitudes, circle_longitudes