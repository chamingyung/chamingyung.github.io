import numpy
import sympy
from sympy import symbols
import matplotlib as plt


from pyscript import document
from pyscript import display

points = []
xlist = []
ylist = []

def point(event) : 
    for i in range(1, 7):  # Assuming you have elements with IDs data_1_x, data_1_y, data_2_x, data_2_y
        data_x = document.querySelector("#data_" + str(i) + "_x")
        data_y = document.querySelector("#data_" + str(i) + "_y")
        data_x = float(data_x.value)
        data_y = float(data_y.value)
        points.append((data_x, data_y)) 

    output_x = document.querySelector("#output_x")
    output_x.innerText = points

    

    return points

func = 0

def poly3(event) : 
    global points
    global func
    for (x,y) in points : 
        xlist.append(x)
        ylist.append(y)
    x_array = numpy.array(xlist)
    y_array = numpy.array(ylist)
    coefficients = numpy.polyfit(x_array, y_array, 3)
    c = coefficients
    x = symbols('x')
    func += c[0]*x**3 + c[1]*x**2 + +c[2]*x + c[3]
    print("다항함수:", func)
    sympy.plot(func, (x,-2, float(max(x_array))+2))
    plt.pyplot.scatter(x_array, y_array, color='blue')

    app_func = document.querySelector("#app_func")
    app_func.innerText = func

    return func

def area(event) : 
    global func
    x_inf = document.querySelector("#x_inf")
    x_sup = document.querySelector("#x_sup")
    x_inf = float(x_inf.value)
    x_sup = float(x_sup.value)
    x = symbols('x')
    F = sympy.integrate(func, x)
    area = F.subs(x,x_sup) - F.subs(x,x_inf)
    val_def_intg = document.querySelector('#val_def_intg')
    val_def_intg.innerText = area 
    


    



        

