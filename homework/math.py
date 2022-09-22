from cmath import pi
import math

def main():
    #pitagorasz tetel
    sideToSolve = input("Give the side you want to solve for (a, b, or c): ")
    if sideToSolve == "a":
        b = float(input("Give side b: "))
        c = float(input("Give side c: "))
        a = math.sqrt(c ** 2 - b ** 2)
        print("The length of the side a is {a}" .format(a))

    elif sideToSolve == "b":
        a = float(input("Give side a: "))
        c = float(input("Give side c: "))
        b = math.sqrt(c ** 2 - a ** 2)
        print("The length of the side b is {b}" .format(b))
    elif sideToSolve == "c":
        a = float(input("Give side a: "))
        b = float(input("Give side b: "))
        c = math.sqrt(a ** 2 + b ** 2)
        print("The length of the side c is {c}" .format(c))
    else:
        print("Only sides acceptable: a, b, c")

    #teglatest terfogata
    sideA = int(input("Side a: "))
    sideB = int(input("Side b: "))
    sideC = int(input("Side c: "))

    V = sideA * sideB * sideC
    print("The volume is {0}" .format(V))

    #kup felszin

    radius = float(input("Enter radius of the cone: "))
    height = float(input("Enter height of the cone: "))

    area = pi * radius * (radius + math.sqrt(radius*radius + height*height))

    print("Area of cone = {0}" .format(area))

if __name__ == "__main__":
    main()