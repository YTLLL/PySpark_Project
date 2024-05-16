#!/bin/bash

# Usage: ./this_script.sh /path/to/output bucket-name /path/to/json "City1,City2,City3"

# Assign positional parameters to variables
output_folder=$1
bucket_name=$2
json_file=$3
cities=$4

# Split the cities by comma and replace commas with spaces for the Python script input
allcities="${cities//,/ }"

# Execute Python script
python3 download.py --output_folder "$output_folder" --json_path "$json_file" --cities $cities

# Copy each city's directory to the Google Cloud Storage bucket
for city in ${allcities}
do
    echo "Moving ${output_folder}/${city} to ${bucket_name}/${city}"
    gsutil -m cp -r "${output_folder}/${city}" "${bucket_name}"
done
