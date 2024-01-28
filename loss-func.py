import sympy
import numpy
from sympy import symbols


from pyscript import document

xlist = []
ylist = []


def make_list(event) : 
    for i in range(1, 9):  # Assuming you have elements with IDs data_1_x, data_1_y, data_2_x, data_2_y
        data_x = document.querySelector("#data_" + str(i) + "_x")
        data_y = document.querySelector("#data_" + str(i) + "_y")

        xlist.append(data_x.value)
        ylist.append(data_y.value)

    output_x = document.querySelector("#output_x")
    output_x.innerText = xlist

    output_y = document.querySelector("#output_y")
    output_y.innerText = ylist

a = 0

x = symbols('x')




def make_loss_func(event) : 
    
    global a
    global xlist
    global ylist

    print(xlist)
    
    xlist_ = []
    ylist_ = []
    x = symbols('x')
    for x_, y_ in zip(xlist, ylist) : 
        x_ = float(x_)
        y_ = float(y_)
        xlist_.append(x_)
        ylist_.append(y_)
        print(xlist_)
        a += (y_ - x*x_)**2
        print('a:', a)
        print(type(a))
        

    a = a / len(xlist)

    loss_func = sympy.expand(a)

    c2 = loss_func.coeff(x,2)
    c1 = loss_func.coeff(x,1)
    c0 = loss_func.coeff(x,0)

    k = str(loss_func)
    print(type(k), k)

    output_loss_func = document.querySelector("#loss_func")
    output_loss_func.innerText = k



        


