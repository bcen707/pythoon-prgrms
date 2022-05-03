# version as a call function accepting args
def area_of_triangle2(base, height, unit):
    x = base
    y = height
    measured_in = unit.lower()
#   print(type(measured_in))     debug
    if (x <= 0 or y <= 0):
       raise ValueError("Entered values must be positive.")
    if (measured_in != "cm" and measured_in != "in" and measured_in != "ft" and measured_in != "m"):   
        raise ValueError("Enter a unit measurement of ft, in, m or cm.")

    else:    
        area = 0.5 * x * y
        print("Area: ",area, measured_in)
