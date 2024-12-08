import math
import matplotlib.pyplot as plt
import numpy as np

def my_func(x,b):
    if x*b > 1 and x*b < 10:
        result = math.exp(x**2)
    elif x*b > 12 and x*b < 40:
        result = math.sqrt(x**2+ 4*b)
    else:
        result = b*((x**2)**2)
    return result

# 2 variant
def other_func(x,y):
    if y == 0:
        result = 0
    elif x == 0:
        result = ((x**2)**2 + y)**3
    elif x/y > 0:
        result = math.log(x**2) + ((x**2)**2 + y)**3
    elif x/y < 0:
        result = math.log(abs((x**2)/y)) + (x**2 + y)**3
    return result

def first_plot(b, y):

    X = np.linspace(-2,2,50)
    Y1 =  []
    Y2 = []
    for x_i in X:
        Y1.append(my_func(x_i, b))
        Y2.append(other_func(x_i, y))

    fig,ax = plt.subplots(figsize=(8, 6))


    # Добавляем графики
    ax.plot(X, Y1, label='My function', color='b', marker='o')
    ax_second = ax.twinx()
    ax_second.plot(X, Y2, label ='Other function', color = 'r', marker='o')

    handles, labels = [], []
    for axes in (ax, ax_second):
        h, l = axes.get_legend_handles_labels()
        handles.extend(h)
        labels.extend(l)


    # Настройки
    ax.set_title('Graphic', fontsize=16)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.legend(handles, labels, loc = 'best', fontsize = 12)
    ax.annotate('The best ever information', [X[10], Y1[10]])
    ax.annotate('Really important point', [X[25], Y2[25]])
    ax.grid(True)

    # Сохраняем и показываем график
    plt.savefig('graphics/thebestevergraphic.png', dpi=400)
    plt.savefig('graphics/thebestevergraphic.pdf', dpi=400)
    return plt