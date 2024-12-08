import matplotlib.pyplot as plt

def fifth_plot():
    films = {
    'Comedy' : 33.1,
    'Fantastic': 21.5,
    'Horror': 10.4,
    'Fighter': 9.68,
    'Drama/melodrama': 6.99}

    plt.subplot()
    plt.bar(films.keys(),films.values(), color = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange'])
    plt.title('Popularity of movie categories: BAR', fontsize = 16)
    plt.xlabel('Categories')
    plt.ylabel('Y axis, procents')
    plt.savefig('graphics/thebesteverbar.png', dpi=400)
    plt.savefig('graphics/thebesteverbar.pdf', dpi=400)
    return plt