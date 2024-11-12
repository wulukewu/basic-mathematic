import pickle
import matplotlib.pyplot as plt

# Load the figure from the pickle file
with open('scatter_plot.pkl', 'rb') as f:
    data = pickle.loads(f.read())

# Display the plot
data.show()