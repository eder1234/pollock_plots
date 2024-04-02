import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the DataFrame from the pickle file
master_file_path = 'master_08052022.pkl'
df = pd.read_pickle(master_file_path)

# Define a color for each unique quantity
color_map = {
    '0': 'red',
    '1u': 'blue',
    '100n': 'green',
    '10n': 'orange'
}

# Folder to save the plots
folder_name = 'cluster_plots'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Get unique clusters
clusters = df["cluster"].unique()

# Iterate over each cluster
for cluster in clusters:
    plt.figure(figsize=(10, 6))
    cluster_data = df[df['cluster'] == cluster]

    for _, row in cluster_data.iterrows():
        traj = row['traj']
        quantity = row['quantity']

        # Split the trajectory into x and y components
        x, y = traj

        # Plot the trajectory with the color corresponding to the quantity
        plt.plot(x, y, color=color_map[quantity], label=quantity, alpha=0.7)

    plt.title(f'Trajectories for Cluster {cluster}')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Create a legend, but avoid duplicate labels
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # Save the plot in the specified folder with a descriptive filename
    plt.savefig(f'{folder_name}/cluster_{cluster}.png')

    # Close the figure to free memory
    plt.close()
