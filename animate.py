import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# load the data
pop_data = pd.read_csv('cleaned-un-country-data.csv')
# filter the data for the year 2020
pop_data_2020 = pop_data[pop_data['Year'] == 2020]
# create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
# set the title and labels
ax.set_title('Population of Countries in 2020')
ax.set_xlabel('Country')
ax.set_ylabel('Population')
# set the x-ticks to the country names
ax.set_xticks(range(len(pop_data_2020['Country'])))
ax.set_xticklabels(pop_data_2020['Country'], rotation=90)
# set the y-axis limit
ax.set_ylim(0, pop_data_2020['Population'].max() * 1.1)
# create a bar chart
bars = ax.bar(pop_data_2020['Country'], pop_data_2020['Population'], color='blue')