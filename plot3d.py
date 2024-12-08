import matplotlib.pyplot as plt
import numpy as np

def seventh_plot():
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    x,y = np.meshgrid(x,y)
    z = np.sin(np.sqrt(x**2+y**2))

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x,y,z)
    ax.set_zlim(-1,1)
    ax.grid(True)

    plt.savefig('graphics/thebestever3d.png', dpi=400)
    plt.savefig('graphics/thebestever3d.pdf', dpi=400)
    return plt