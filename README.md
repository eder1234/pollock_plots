
# Cluster Trajectories Visualization

This Python script reads a dataset from a pickle file and visualizes trajectories for different clusters. Each trajectory is colored based on a predefined quantity value. The plots are saved in a designated folder named `cluster_plots`.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.9
- NumPy
- pandas
- Matplotlib

## Installation Instructions

1. **Clone the repository or download the script**

   If the code is hosted in a repository, you can clone it using:

   ```
   git clone https://github.com/eder1234/pollock_plots.git
   ```

   Alternatively, download the Python script directly to your local machine.

2. **Set up a Python environment**

   It's recommended to use a virtual environment to manage dependencies. You can set up a virtual environment using the following commands:

   - For **Conda**:

     ```
     conda create --name cluster-env python=3.9
     conda activate cluster-env
     ```

   - For **venv**:

     ```
     python -m venv cluster-env
     source cluster-env/bin/activate  # On Windows use `cluster-env\Scripts\activate`
     ```

3. **Install dependencies**

   Navigate to the directory containing the `requirements.txt` file and run:

   ```
   pip install -r requirements.txt
   ```

   This will install the required packages (NumPy, pandas, and Matplotlib) in your environment.

## Running the Script

To run the script, ensure your Python environment is activated and execute:

```
python pollock_plot-0.py
```

## Output

The output plots will be saved in a folder named `cluster_plots` within the same directory as your script. Each plot will be named according to its cluster, for example, `cluster_1.png`, `cluster_2.png`, etc.
