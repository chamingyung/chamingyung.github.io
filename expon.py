import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


from pyscript import document
from pyscript import display

xv = []
yv = []
def point(event) : 
    for i in range(1,6) : 
        data_x = document.querySelector("#data_" + str(i) + "_x")
        data_y = document.querySelector("#data_" + str(i) + "_y")
        data_x = float(data_x.value)
        data_y = float(data_y.value)
        xv.append(data_x)
        yv.append(data_y)
        result1 = document.querySelector('#result1')
        result1.innerText = '전송완료'
    return xv, yv

# xv = np.linspace(0, 9, 10)
# yv = [1, 2.1, 3.9, 7.8, 17, 30, 67.3, 129, 260, 513]

coeff_fitting = 0

def exp_func(event) :
    global coeff_fitting 
    coeff_fitting = np.polyfit(np.exp(xv), yv, 1)
    result_a = document.querySelector('#result_coeff_a')
    result_a.innerText =coeff_fitting[0]
    result_b = document.querySelector('#result_coeff_b')
    result_b.innerText =coeff_fitting[1]
    return coeff_fitting

def plot_1(event) : 
    plt.scatter(xv, yv, color='blue')
    plt.title('산점도')
    plt.show()


    
def plot_2(event) : 
    x = sy.symbols('x')
    exp_fitting_func = coeff_fitting[0] * sy.exp(x) + coeff_fitting[1]
    # SymPy의 식을 수치로 변환
    exp_fitting_func_numeric = sy.lambdify(x, exp_fitting_func, 'numpy')
    # SymPy의 plot 함수를 사용하지 않고 plt.plot으로 지수 함수 그리기
    x_vals = np.linspace(xv[0] - 1, xv[-1] + 1, 100)
    plt.plot(x_vals, exp_fitting_func_numeric(x_vals), label='Exponential Fit', color='crimson')

    # Matplotlib을 사용하여 산점도 추가
    plt.scatter(xv, yv, label='Data Points', color='blue')

    # 그래프에 레이블 등 추가
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()








