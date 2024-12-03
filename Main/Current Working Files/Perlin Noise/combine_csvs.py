import pandas as pd

# List of file paths for the three CSV files
csv_files = ['Perlin Noise\perlin_noise_analysis1-2.csv', 
             'Perlin Noise\perlin_noise_analysis1-3.csv',
             'Perlin Noise\perlin_noise_analysis1.csv',
             'Perlin Noise\perlin_noise_analysis2-1.csv',
             'Perlin Noise\perlin_noise_analysis2-2.csv']

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through the file paths and read each CSV file into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all the DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new CSV file
output_file = r'Salt and Pepper Noise\combined_SnP.csv'
combined_df.to_csv(output_file, index=False)

print(f"Combined CSV saved as {output_file}")
