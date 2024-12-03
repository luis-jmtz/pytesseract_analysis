import pandas as pd

# List of file paths for the CSV files
csv_files = [
    'SnP_noise_analysis.csv',
    'SnP_noise_v2-1_analysis.csv',
    'SnP_noise_v2-2_analysis.csv',
    'SnP_noise_v2-3_analysis.csv'
]

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through the file paths and read each CSV file into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all the DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Select only numeric columns and ensure grouping column is included
numeric_columns = combined_df.select_dtypes(include='number').columns
grouped_df = combined_df.groupby('Noise Strength', as_index=False)[numeric_columns].mean()

# Save the grouped DataFrame to a new CSV file
output_file = 'combined_SnP_v2.csv'
grouped_df.to_csv(output_file, index=False)

print(f"Grouped and averaged CSV saved as {output_file}")
