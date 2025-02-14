import os
import sys
import subprocess

# Process all CSV files in a folder
folder_path = sys.argv[1] # Set the path to the folder containing the CSV files
output_dir = sys.argv[2]
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

for csv_file in csv_files:
    full_path = os.path.join(folder_path, csv_file)
    print(f"Processing {full_path}")
    process = ['python',
    'get_features_CTransPath.py',
    str(folder_path + '/'+csv_file),
    output_dir
    ]
    subprocess.run(process, capture_output=True,
                                    text=True, check=True)


    # Add any specific processing code here

