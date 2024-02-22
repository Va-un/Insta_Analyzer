import os

import pandas as pd
import datetime
from Functions import *

input_dir ='instagram-varun_yeager-2024-02-18-fJ87WRXU\your_instagram_activity\messages\inbox'
output_dir = 'Message'





#Json_csv(input_dir,output_dir)
#perprocessor(output_dir)




def Text_Cleaner(Prep_input, specific_text):
    files = os.listdir(Prep_input)
    for file in files:
        df = pd.read_csv(os.path.join(Prep_input, file))

        # Drop rows containing specific text in 'content' column
        df = df[~df['content'].str.contains(specific_text)]

        df.to_csv(os.path.join(Prep_input, file), index=False)


' sent an attachment'


