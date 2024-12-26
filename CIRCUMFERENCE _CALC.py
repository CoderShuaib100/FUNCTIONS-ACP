# creating the function
def Circumference(R):
    ans = 2 * 3.14 * R
    print("The circumference of the circle of radius",R,"is", ans,".")

radius = float(input("Enter a the radius of a circle: "))

Circumference(radius)