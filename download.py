import json
import os
import requests
import gzip
import shutil
import argparse

def download_and_upload_data(json_path, output_folder, cities_to_process):
    # Load city and URL data from a JSON file
    with open(json_path, 'r') as file:
        city_urls = json.load(file)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for city in cities_to_process:
        base_url = city_urls.get(city)
        if not base_url:
            print(f"No URL found for {city}. Skipping...")
            continue
        
        # Create a directory for the city
        print("Creating folder for ", city)
        city_dir = os.path.join(output_folder, city)
        if not os.path.exists(city_dir):
            os.makedirs(city_dir)

        # Download and process each file type
        print("Download data for ", city)
        for file_name in ['reviews.csv.gz', 'listings.csv.gz']:
            print("Download ", file_name)
            # Construct the URL
            file_url = f"{base_url}{file_name}"

            # Download the file
            response = requests.get(file_url)
            if response.status_code != 200:
                print(f"Failed to download {file_url}")
                continuejs
            gz_path = os.path.join(city_dir, file_name)
            with open(gz_path, 'wb') as f:
                f.write(response.content)

            # Unzip the file
            print("Unzip the file ", file_name)
            with gzip.open(gz_path, 'rb') as f_in:
                with open(gz_path[:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            # Remove the .gz file
            print("Remove the gz file ", file_name)
            os.remove(gz_path)

def main():
    parser = argparse.ArgumentParser(description="Download AirBnB data to local")
    parser.add_argument("--output_folder", help="Path to the output folder where files will be stored locally")
    parser.add_argument("--json_path", help="Path to the JSON file containing city URLs")
    parser.add_argument("--cities", help="List of cities to process")
    args = parser.parse_args()

    download_and_upload_data(args.json_path, args.output_folder, args.cities.split(','))

if __name__ == "__main__":
    main()