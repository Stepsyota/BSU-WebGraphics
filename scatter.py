import matplotlib.pyplot as plt
import numpy as np

def second_plot():
    fig, ax = plt.subplots(figsize=(8, 8))

    x1 = np.random.normal(1,0.5,50)
    y1 = np.random.normal(2,0.5,50)

    x2 = np.random.normal(3,0.5,50)
    y2 = np.random.normal(5,0.5,50)

    x3 = np.random.normal(2,0.5,50)
    y3 = np.random.normal(6,0.5,50)

    ax.scatter(x1,y1, label = 'Cluster 1')
    ax.scatter(x2,y2, label = 'Cluster 2')
    ax.scatter(x3,y3, label = 'Cluster 3')

    ax.set_title('Scatter graphic', fontsize = 16)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.legend(loc = 'best')
    ax.grid(True)
    # Сохраняем и показываем график
    plt.savefig('graphics/thebesteverscatter.png', dpi=400)
    plt.savefig('graphics/thebesteverscatter.pdf', dpi=400)
    return plt