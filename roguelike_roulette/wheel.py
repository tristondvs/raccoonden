from matplotlib import pyplot as plot
import numpy as num

# Creating list
games = ['Heroes of Hammerwatch', 'Hades', 'Vampire Survivors', 'Beacon', 'Inscryption']
value = len(games)/100

# creating the graph
pieg = plot.figure(figsize =(10, 7))
plot.pie(value, labels = games)

plot.show()
