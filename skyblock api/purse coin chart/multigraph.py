
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x']
    pursedata = data['purse1']
    pursedata2 = data['purse2']
    pursedata3 = data['purse3']

    plt.cla()

    plt.plot(x, pursedata, label='Account 1')
    plt.plot(x, pursedata2, label='Account 2')
    plt.plot (x, pursedata3, label='Account 3')
    plt.ylim(ymin=150,ymax=1800)
    plt.ylabel("Coins (Millions)")

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=28000)

plt.tight_layout()
plt.show()