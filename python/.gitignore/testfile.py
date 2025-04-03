import pandas as pd 
import matplotlib.pyplot as plt

file_path = "sample_data.xlsx"
df = pd.read_excel(file_path)
print(df)
plt.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o', linestyle='-', color='b', label="Line 1")

# Add labels and title
plt.xlabel("X-axis Label")  # Change as per your data
plt.ylabel("Y-axis Label")  # Change as per your data
plt.title("Sample Graph")
plt.legend()

# Show the plot
plt.show()