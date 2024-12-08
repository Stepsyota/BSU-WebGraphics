import matplotlib.pyplot as plt
import numpy as np

def fourth_plot():
    plt.subplot()

    matrix = np.random.rand(10,10)

    plt.imshow(matrix, cmap = 'viridis')
    plt.colorbar()
    plt.title('My heatmap', fontsize = 16)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    for i in range(10):
        for j in range(10):
            plt.text(i, j, round(matrix[i, j],2),ha='center', va='center', color='black')

    plt.savefig('graphics/thebesteverheatmap.png', dpi=400)
    plt.savefig('graphics/thebesteverheatmap.pdf', dpi=400)
    return plt