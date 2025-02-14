import h5py
import csv
import numpy as np
import os

directory = 'MSI_features_per_patient' # contains csv files with embedding table for each slide
out_directory = 'h5_embeddings_per_patient'
output_csv = 'slides_all_per_patient_msi.csv'

# Loop through all files in the directory
with open(output_csv, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header
    csv_writer.writerow(['FILENAME', 'PATIENT'])

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv') and filename.startswith('embeds_'):
            # Construct the full path to the file
            csv_path = os.path.join(directory, filename)

            # Load the CSV file into a numpy array
            arr1 = np.loadtxt(csv_path, delimiter=",", dtype=float)

            # Slice the array to remove the last column containing the label
            arr1_768 = arr1[:, :-1]

            # Construct the output H5 file name
            basename = filename.replace('embeds_', '').replace('.csv', '.h5')
            h5_path = os.path.join(out_directory, basename)

            # Save the processed array to the H5 file
            with h5py.File(h5_path, 'w') as f:
                f.create_dataset('features', data=arr1_768)
                f.create_dataset('coords', data=0)

            # Extract the patient identifier (first part of the name before the underscore)
            patient_id = filename.split('_')[3]

            # Write the basename (without .h5 extension) and patient_id to the CSV file
            csv_writer.writerow([basename.replace('.h5', ''), basename.replace('.h5', '')])

            print(f"Processed {filename} and saved to {basename}")

print(f"Basenames and patient IDs written to {output_csv}") # Creates slide.csv for HistoBistro
