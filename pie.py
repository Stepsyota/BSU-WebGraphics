import matplotlib.pyplot as plt

def third_plot():
    films = {
    'Comedy' : 33.1,
    'Fantastic': 21.5,
    'Horror': 10.4,
    'Fighter': 9.68,
    'Drama/melodrama': 6.99}

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(films.values(), labels = films.keys(), autopct='%1.1f%%')
    ax.set_title('Popularity of movie categories', fontsize = 16)
    ax.grid(True)
    plt.savefig('graphics/thebesteverpie.png', dpi=400)
    plt.savefig('graphics/thebesteverpie.pdf', dpi=400)
    return plt