from math import sin, cos, sqrt, radians, asin

def distance(location1: tuple, location2: tuple):
    lat1, lon1 = location1
    lat2, lon2 = location2

    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    dis = R * c
    return dis

def main():
    lat1 = 53.32055555555556
    lat2 = 53.31861111111111
    lon1 = -1.7297222222222221
    lon2 =  -1.6997222222222223
    print(distance((lat1, lon1), (lat2, lon2)), "K.M")
    return 0

if __name__ == "__main__":
    main()