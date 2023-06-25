import scipy.io
import numpy as np
import csv


def mat_to_csv(mat_file, csv_file):
    # Load .mat file
    data = scipy.io.loadmat(mat_file)

    # Extract variables from .mat file
    variable_names = [name for name in data if not name.startswith('__')]
    if len(variable_names) != 1:
        raise ValueError("The .mat file should contain exactly one variable.")

    # Get the variable data
    variable_data = data[variable_names[0]]

    # Convert data to numpy array (if not already)
    if not isinstance(variable_data, np.ndarray):
        variable_data = np.array(variable_data)

    # Write the data to .csv file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(variable_data)


# Example usage
mat_file = 'imagelabels.mat'
csv_file = 'imagelabels.csv'
mat_to_csv(mat_file, csv_file)
