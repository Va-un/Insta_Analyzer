import pandas as pd

import os
import json

def Json_csv(input_dir, output_dir):
    input_dir_list = os.listdir(input_dir)
    merged_df = pd.DataFrame()  # Initialize an empty DataFrame to store merged data

    for name in input_dir_list:
        json_file = os.path.join(input_dir, name)
        file_name = os.listdir(json_file)[0]
        file = os.path.join(json_file, file_name)
        json_file_path = file

        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)
                message_data = json_data['messages']
                df = pd.json_normalize(message_data)
                df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
                df['timestamp_year'] = df['timestamp_ms'].dt.strftime('%Y-%m-%d')
                df['timestamp_time'] = df['timestamp_ms'].dt.strftime('%H:%M:%S')
                df.drop(columns=['timestamp_ms', 'is_geoblocked_for_viewer'], inplace=True)



                # Merge current DataFrame with the merged DataFrame
                merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print(f'File "{json_file_path}" does not exist.')

    # Write the merged DataFrame to a CSV file in the output directory
    merged_csv_path = os.path.join(output_dir, 'merged_data.csv')
    merged_df.drop(columns=['photos', 'audio_files', 'videos', 'share.profile_share_username', 'share.profile_share_name',
                          'call_duration', 'is_unsent', 'share.link'], inplace=True)

    merged_df['content'] = merged_df['content'].fillna('')  # Fill NaN values with an empty string
    merged_df = merged_df[~merged_df['content'].str.contains('sent an attachment')]

    merged_df.to_csv(merged_csv_path, index=False)
    print(f'Merged data saved to "{merged_csv_path}".')
