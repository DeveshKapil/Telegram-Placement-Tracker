import csv
import random

# Function to read CSV file and randomize rows
def randomize_csv(input_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        random.shuffle(data)  # Shuffle rows randomly

    return data

# Function to write data to new CSV file with 200 rows per file
def write_csv_divided(data, output_prefix):
    num_files = (len(data) + 199) // 200  # Calculate number of files needed

    for i in range(num_files):
        start_idx = i * 200
        end_idx = min((i + 1) * 200, len(data))
        output_file = f"{output_prefix}_{i + 1}.csv"  # Output file name

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data[start_idx:end_idx])

# Input and Output file paths
input_file_path = 'sample_100.csv'  # Replace 'input.csv' with your input CSV file path
output_prefix = 'output'  # Prefix for output CSV files

# Randomize rows of input CSV file
randomized_data = randomize_csv(input_file_path)

# Write randomized data to new CSV files with 200 rows per file
write_csv_divided(randomized_data, output_prefix)
