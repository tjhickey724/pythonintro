import math
def cylinder_volume(radius, height):
    base_area = math.pi*radius**2
    volume = base_area*height
    return(volume)

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius**2
    base_circumference = 2*math.pi * radius
    side_area = base_circumference * height
    return 2*base_area + side_area

def calc_cylinder_stats():
    print("Cylinder Calculator")
    r = float(input("radius: "))
    h = float(input("height: "))
    volume = cylinder_volume(r,h)
    area = cylinder_surface_area(r,h)
    print(f'The volume of a cylinder of radius {r} and height {h} is {volume}')
    print(f'and the surface area is {area}')

calc_cylinder_stats()
