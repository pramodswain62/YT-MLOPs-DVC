import pandas as pd
import os

data = {'name': ['alice', 'bob', 'charlei'],
        'Age': [30,20,25],
        'city': ['nk', 'dl', 'mb']}

df = pd.DataFrame(data)

new_row_loc = {'name':'gf1', 'Age': 20, 'city':'kl'}
df.loc[len(df.index)]= new_row_loc

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)
print('csv file saved to ', file_path)