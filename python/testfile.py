import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

def plot_data():
    # Create a sample DataFrame
    data = {
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100))
    }
    df = pd.DataFrame(data)

    # Plot the data
    plt.plot(df['x'], df['y'])
    plt.title('Sine Wave')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
if __name__ == "__main__":  
    plot_data()
    