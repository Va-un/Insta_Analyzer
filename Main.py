import os
import time

from Functions import *

input_dir ='instagram-varun_yeager-2024-02-18-fJ87WRXU\your_instagram_activity\messages\inbox'
output_dir = 'Message'





#Json_csv(input_dir, output_dir)
df = pd.read_csv('Message/merged_data.csv')

from tqdm import tqdm


for index in tqdm(range(len(df))):
    df.at[index, 'English_Translation'] = translate_to_english(df.at[index, 'content'])

