import pandas as pd

import os
import json



def perprocessor(Prep_input):
    files = os.listdir(Prep_input)
    for file in files:
        df = pd.read_csv(os.path.join(Prep_input,file))
        # Convert milliseconds to seconds and then to datetime objects
        df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')

        # Convert to a readable format if needed
        df['timestamp_year'] = df['timestamp_ms'].dt.strftime('%Y-%m-%d')
        df['timestamp_time'] = df['timestamp_ms'].dt.strftime('%H:%M:%S')
        df.drop(columns=['timestamp_ms','is_geoblocked_for_viewer'],inplace=True)
        df.to_csv(os.path.join(Prep_input,file))


def Json_csv(input_dir,output_dir):
    input_dir_list = os.listdir(input_dir)

    
    for name in list(input_dir_list):
        json_file = os.path.join(input_dir, name)

        file_name = os.listdir(json_file)[0]
        file = os.path.join(json_file, file_name)
        json_file_path = file
    # Check if the file exists
        if os.path.exists(json_file_path):
            # Open the file in read mode
            with open(json_file_path, 'r') as file:
                # Load JSON data
                json_data = json.load(file)
                message_data = json_data['messages']
                normalized_data = pd.json_normalize(message_data)
                normalized_data.to_csv(os.path.join(output_dir, name+ '.csv'),index=False)

        else:
            print(f'File "{json_file_path}" does not exist.')


def Text_Cleaner(Prep_input, specific_text):
    files = os.listdir(Prep_input)
    for file in files:
        df = pd.read_csv(os.path.join(Prep_input, file))

        # Drop rows containing specific text in 'content' column
        df = df[~df['content'].str.contains(specific_text)]

        df.to_csv(os.path.join(Prep_input, file), index=False)