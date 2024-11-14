## Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# length = float(input("What is the length of the room, in meters?  "))
# width = float(input("What is the width of the room, in meters?  "))

# area_meters = length * width
# area_feet = area_meters * 10.7639

# print(f"Area: {area_meters:.2f} square meters, or {area_feet:.2f} square feet")


## Modify the program to let the user specify the measurement type (meters or feet). 
## Compute the area accordingly and print it and its conversion in parentheses.

measurement_type = input('Measurement type? Answer "meters" or "feet": ').lower()
length = float(input("What is the length of the room?  "))
width = float(input("What is the width of the room?  "))

area = length * width

if measurement_type == 'feet':
    ft2m = area / 10.7639
    print(f"Area: {area:.2f} square feet ({ft2m} square meters)")
else:
    m2ft = area * 10.7639
    print(f"Area: {area:.2f} square meters ({m2ft} square feet)")
