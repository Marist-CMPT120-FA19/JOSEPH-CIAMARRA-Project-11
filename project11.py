import math

class Sphere:
    def __init__(s, radius):
        s.radius = radius
        s.area = 0
        s.volume = 0

    def getRadius(s):
        return s.radius

    def surfaceArea(s):
        s.a = 4 * math.pi * (s.radius**2)
        return (s.a)

    def getVolume(s):
        s.v = (4/3) * math.pi * (s.radius**3)
        return (s.v)

def main():
    radius = eval(input("Enter a radius: "))
    r = radius
    rad = Sphere(r)

    print("Area: ", rad.surfaceArea())
    print("Volume: ", rad.getVolume())

main()
