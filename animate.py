import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def add_year_text(ax, year):
    """Add year text to the plot."""
    ax.text(0.9, 0.15, str(year), transform=ax.transAxes, fontsize=20,
            ha='center', va='top', bbox=dict(facecolor='white', alpha=0.5))
# load the data
def create_animation(df):
    df = pd.read_csv('cleaned-un-country-data.csv')

    frames = df['Time'].unique()

    fig, ax = plt.subplots(figsize=(12, 6))

    def animate(frame):
        ax.clear()
        pop_data_frame = df[df['Time'] == frame]
        top_pop = pop_data_frame.nlargest(10, 'TPopulation1Jan').sort_values(by='TPopulation1Jan', ascending=True).reset_index(drop=True)
        

        ax.barh(top_pop['Location'], top_pop['TPopulation1Jan'], color='blue')
        for i, row in top_pop.iterrows():
            ax.text(row['TPopulation1Jan'], i, f"{row['TPopulation1Jan']:,}", va='center', fontsize=10)
        
        ax.set_title(f'Top 10 Countries by Population in {frame}')
        ax.set_xlabel('Population on 1st January')
        ax.set_ylabel('Country')
        
        add_year_text(ax, frame)
        fig.tight_layout()

    anim = FuncAnimation( fig, animate, frames=frames, repeat=True, interval=200)
    return anim

if __name__ == "__main__":
    df = pd.read_csv('cleaned-un-country-data.csv')
    anim = create_animation(df)
    
    
    #anim.save('population_animation.mp4', writer='ffmpeg', fps=10)
    plt.show()
