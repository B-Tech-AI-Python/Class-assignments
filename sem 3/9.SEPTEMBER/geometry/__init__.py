from geometry import area
from geometry import volume

while True:

    try:
        # area or volume
        input_string = input("Do you want area or volume? ")

        # for area        
        if input_string.lower().startswith('a'):
            func = input("Do you want area of rectangle or circle? ")

            # for rectangle area
            if func.lower().startswith('r'):
                length = int(input("Enter length: "))
                breadth = int(input("Enter breadth: "))

                rectangle_area = area.rectangle_area(length,breadth)
                print(f"Area of rectangle: {rectangle_area}")
                break

            # for circle area
            elif func.lower().startswith('c'):
                radius = int(input("Enter radius: "))
                
                circle_area = area.circle_area(radius)
                print(f"Volume of sphere: {circle_area}")
                break

            # else
            else:
                raise ValueError

            # break out of loop
            break

        # for volume
        elif input_string.lower().startswith('v'):
            func = input("Do you want volume of cuboid or sphere? ")

            # for cuboid volume
            if func.lower().startswith('c'):
                length = int(input("Enter length: "))
                breadth = int(input("Enter breadth: "))
                height = int(input("Enter height: "))

                cuboid_volume = volume.cuboid_volume(length,breadth,height)
                print(f"Area of rectangle: {cuboid_volume}")
                break

            # for sphere volume
            elif func.lower().startswith('s'):
                radius = int(input("Enter radius: "))
                
                volume_sphere = volume.sphere_volume(radius)
                print(f"Volume of sphere: {volume_sphere}")
                break

            # else
            else:
                raise ValueError
            
            # break out of loop
            break

        # outer else
        else:
            raise ValueError

    # ValueError statement
    except ValueError:
        print("Wrong input! Try again!")
