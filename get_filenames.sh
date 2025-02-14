#!/bin/bash

# Define the top-level directory
#TOP_LEVEL_DIR="../Mayo_CRC_MSI_patches" # This dir should have the subdirectories for each slide containing patches
TOP_LEVEL_DIR="../MSS_patches_per_patient" # This dir should have the subdirectories for each slide containing patches

# Get user input for the label
# MSS = 0, MSI = 1
read -p "Enter label (0 or 1): " LABEL

# Function to create CSV for each img_dir_n
create_csv() {
    local IMG_DIR="$1"
    local CSV_FILE="$IMG_DIR.csv"
    # Iterate over image files in the img_dir_n directory
    find "$IMG_DIR" -type f -name "*.jpg" | while read -r FILE; do
        # Print filename and label to CSV file
        echo "$FILE,$LABEL" >> "$CSV_FILE"
    done
}

# Iterate over img_dir_n directories
for DIR in "$TOP_LEVEL_DIR"/*; do
    if [ -d "$DIR" ]; then
        # Check if it's a directory
        IMG_DIR_NAME=$(basename "$DIR")
        # Create CSV for the img_dir_n
        create_csv "$DIR"
    fi
done
#!/bin/bash

# Define the top-level directory
TOP_LEVEL_DIR="/path/to/WSIs_extraction" # This dir should have the subdirectories for each slide containing patches

# Get user input for the label
# MSS = 0, MSI = 1
read -p "Enter label (0 or 1): " LABEL

# Function to create CSV for each img_dir_n
create_csv() {
    local IMG_DIR="$1"
    local CSV_FILE="$IMG_DIR.csv"
    # Iterate over image files in the img_dir_n directory
    find "$IMG_DIR" -type f -name "*.jpg" | while read -r FILE; do
        # Print filename and label to CSV file
        echo "$FILE,$LABEL" >> "$CSV_FILE"
    done
}

# Iterate over img_dir_n directories
for DIR in "$TOP_LEVEL_DIR"/*; do
    if [ -d "$DIR" ]; then
        # Check if it's a directory
        IMG_DIR_NAME=$(basename "$DIR")
        # Create CSV for the img_dir_n
        create_csv "$DIR"
    fi
