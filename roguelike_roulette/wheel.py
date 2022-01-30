from tkinter import *
#import matplotlib
#from matplotlib import pyplot as plot
#matplotlib.use('Agg')
#import numpy as num

def populate_list():
    print('Populate')

def add_game():
    print('Added Game')

def remove_game():
    print('Removed Game')

# create window object
app = Tk()

# Add games to list
game_name = StringVar()
games_label = Label(app, text='Enter Game Name', font=('bold', 14), pady=5, padx=20)
games_label.grid(row=0, column=0, sticky=W)
games_entry = Entry(app, textvariable=game_name)
games_entry.grid(row=0, column=1)
#Show a list of games
games_list = Listbox(app, height=15, width=40, border=1)
games_list.grid(row=1, column=0, columnspan=1, rowspan=1, padx=20, pady=10)
# Adding a scroll bar
#scrollbar = Scrollbar(app)
#scrollbar.grid(row=1, column=0)
# Bind the scrollbar to the list of games
#games_list.configure(yscrollcommand=scrollbar.set)
#scrollbar.configure(command=games_list.yview)

# Adding buttons
add_button = Button(app, text='Add Game', width=12, command=add_game)
add_button.grid(row=0, column=2, padx=10)
#remove_button = Button(app, text='Remove Game', width=12, command=remove_game)
#add_button.grid(row=4, column=4, pady=20)

app.title('Roguelike Roulette Spinwheel')
#Adjust the size of the window when the app opens
app.geometry('600x600')



# creating the graph
#pieg = plot.figure(figsize =(10, 7))
#plot.pieg(value, labels = games)

#plot.show()



## TODOS:
# Prepare a UI that will allow users to input games, and click the 'Add' Button.
# - We can also remove them from the list
# Take the list of games and make them into a pie chart with equal values, so it looks similar to a wheel of choices
# - We can give them an equal value by doing something like value = len(games_list) / 100
# Find a way to make the wheel spin and lands on a choice
# Find a way to determine the string within the object

# Start program
app.mainloop()
