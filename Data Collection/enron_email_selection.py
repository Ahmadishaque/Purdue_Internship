import pandas as pd
import random

# Set the number of rows to randomly sample
num_rows_to_sample = 19661

# Load the existing Excel file into a pandas DataFrame
existing_excel_file = 'emails.csv'
df = pd.read_csv(existing_excel_file)


# Randomly sample the specified number of rows from the DataFrame
random_sampled_df = df.sample(n=num_rows_to_sample, random_state=42)

# Save the sampled data to a new Excel file called "enron.xlsx"
new_excel_file = 'enron_data.xlsx'
random_sampled_df.to_excel(new_excel_file, index=False)

print(f"{num_rows_to_sample} rows randomly sampled and saved to {new_excel_file}.")
