#import pandas as pd

#def count_rows_with_country(file_path, country_name):
#    df = pd.read_csv(file_path)
#    return df[df['Country'] == country_name].shape[0]
#archive/South America towers.csv
#file_path = 'archive/South America towers.csv'
#country_name = 'Chile'
#rows_count = count_rows_with_country(file_path, country_name)
#print(f"Number of rows with country {country_name}: {rows_count}")
#
import pandas as pd

def calculate_average_signal(file_path, country_name):
    df = pd.read_csv(file_path)
    filtered_df = df[df['Country'] == country_name]
    if filtered_df.empty:
        return 0
    return filtered_df['averageSignal'].mean()

file_path = 'archive/South America towers.csv'
country_name = 'Chile'
average_signal = calculate_average_signal(file_path, country_name)
print(f"Average signal for {country_name}: {average_signal}")
