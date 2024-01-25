#!/bin/bash

# Set the source and destination directories
source_directory="." # You can change this to the directory where your folders are located
destination_directory="./data"

# Find all folders matching the regex "*.csv/"
folders=($(find "$source_directory" -type d -regex '.*\.csv$'))

# Iterate through the folders and copy the single CSV file inside each folder
for folder in "${folders[@]}"; do
    # Get the folder name
    folder_name=$(basename "$folder")

    # Find the CSV file inside the folder
    csv_file=$(find "$folder" -maxdepth 1 -type f -name '*.csv')

    # Check if a single CSV file is found
    if [ -n "$csv_file" ] && [ $(echo "$csv_file" | wc -l) -eq 1 ]; then
        # Copy the CSV file to the destination with the folder name
        cp "$csv_file" "$destination_directory/$folder_name"
        echo "Copied $csv_file to $destination_directory/$folder_name"
    else
        echo "Skipping $folder as it does not contain a single CSV file."
    fi
done
