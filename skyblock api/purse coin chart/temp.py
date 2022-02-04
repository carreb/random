import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


data = pd.read_csv('data.csv')
x = data['x']
pursedata = data['purse']
mingrabber = pd.read_csv('data.csv')
lastrow = mingrabber['purse'][-1]
getmin = lastrow['purse']
minimumval = getmin-40

print(minimumval)