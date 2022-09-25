Найти самую далёкую планету, даны длины полуосей элептических орбит

list_of_orbits=[(1,3),(2.5,10),(7,2),(6,6),(4,3)]

def find_farthest_orbit(list_of_orbits):
    PI = 3.14
    s=lambda a,b:a*b*PI
    # Находим максималную орбиту orbitMAX
    orbitMAX=max([s(a,b) for a, b in list_of_orbits if a!=b])
    # Находим кортеж с длинами полуосей самой алёкой планеты
    distantPlanet=((a, b) for a, b in list_of_orbits if s(a,b)==orbitMAX)
    return distantPlanet

print(*find_farthest_orbit(list_of_orbits))
