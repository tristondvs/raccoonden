import matplotlib.pyplot as plt

plt.figure(figsize=(3,3))

labels = ['Wendy\'s', 'Burger King', 'McDonalds', 'Jersey Mike\'s']
values = []
for i in labels:
    values.append(len(labels)/100)

plt.pie(values, labels=labels)

plt.show()