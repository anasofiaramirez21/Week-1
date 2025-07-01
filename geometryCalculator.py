import math
# to access math functions and constants like math.pi

# --- Functions ---
def areaRectangle(length, width):
    # Calculate and return the area of a rectangle.
    # Parameters:
    #   length (float): length of the rectangle
    #   width (float): width of the rectangle
    # Returns:
    #   float: area of the rectangle
    return length * width

def areaTriangle(base, height):
    # Calculate and return the area of a triangle.
    # Parameters:
    #   base (float): base length of the triangle
    #   height (float): height of the triangle
    # Returns:
    #   float: area of the triangle
    return 0.5 * base * height

def areaCircle(radius):
    # Calculate and return the area of a circle.
    # Parameters:
    #   radius (float): radius of the circle
    # Returns:
    #   float: area of the circle
    return math.pi * radius * radius

# --- Main Program ---

print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

# these are called conditionals, there will be more information about them next week
# they are meant to check if a condition is true, if so, it runs
# for now, just use this template we gave you :)
if shape == "r":
    # TODO: Ask for length and width as floats
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    # TODO: Calculate area using areaRectangle()
    area = areaRectangle(length, width)
    # TODO: Print the result nicely formatted
    print("The area of the rectangle is " + str(area))
    # print(areaRectangle(2,2)) this was for tesing 
    # print(areaTriangle(1,1))
    # print(areaCircle(1))

elif shape == "t":
    # TODO: Ask for base and height as floats
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    # TODO: Calculate area using areaTriangle()
    area = areaTriangle(base, height)
    # TODO: Print the result nicely formatted
    print("The area of the triangle is " + str(area))

elif shape == "c":
    # TODO: Ask for radius as a float
    radius = float(input("Enter the radius: "))
    # TODO: Calculate area using areaCircle()
    area = areaCircle(radius)
    # TODO: Print the result nicely formatted
    print("The area of the circle is " + str(area))

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
