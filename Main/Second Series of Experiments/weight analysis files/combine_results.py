import pandas as pd

csv_files = ['weight_analysis_v2.csv', 'weight_analysis_v3.csv', 'weight_analysis_v4.csv']

dataframes = []

# Loop through the file paths and read each CSV file into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all the DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

output_file = 'combined.csv'
combined_df.to_csv(output_file, index=False)
