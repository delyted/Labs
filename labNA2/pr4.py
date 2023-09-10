import math

data = {}
with open('D:/Codes/python/labNA2/map.txt') as file:
    next(file)
    next(file)
    for line in file:
        coord_str, elevation_str = line.strip().split('            ')
        coord = tuple(map(int, coord_str.strip('()').split(', ')))
        if 'NaN' in elevation_str:
            elevation = float('nan')
        else:
            elevation = float(elevation_str)
        data[coord] = elevation

def inverse_distance_weighting(coord, data, p=2):
    weights = []
    elevations = []

    for c, e in data.items():
        if not math.isnan(e):
            d = math.sqrt((coord[0] - c[0]) ** 2 + (coord[1] - c[1]) ** 2)
            if d > 0:  # Avoid division by zero
                weight = 1 / d ** p
                weights.append(weight)
                elevations.append(e * weight)

    if not weights:
        return None

    return sum(elevations) / sum(weights)

for coord, elevation in data.items():
    if math.isnan(elevation):
        data[coord] = inverse_distance_weighting(coord, data)

for coord, elevation in data.items():
    print(f"Coordinates: {coord}, Elevation: {elevation}")
