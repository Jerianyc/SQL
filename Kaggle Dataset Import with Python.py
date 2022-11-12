# %%
# This Python code is to be ran in Jupyter Notebooks. I wrote this to make dataset import when working with Kaggle as simple as possible. Feel free to copy for easy dataset install!

# 1. opendatasets will be the tool we use to install the Kaggle dataset
import opendatasets as od

# %%
# 2. Define dataset - PASTE KAGGLE DATA BELOW
dataset = 'https://www.kaggle.com/datasets/ayushmi77al/weather-data-set-for-beginners'

# %%
# 3. Download the dataset. You will be prompted to add Kaggle username and API token. API token can be generated @ https://www.kaggle.com/[USERNAME]/account - COPY the pathname that appears after it downloads
od.download(dataset)

# %%
# 4. OS will be used to show us the name of the CSV with the listdir funtion
import os

# %%
# 5. Pandas is my tool of choice for reading the CSV using the read_csv function
import pandas

# %%
# 6. PASTE pathname from step 3 as the data_dir
data_dir = '.\weather-data-set-for-beginners'

# %%
# 7. Lists files from within the directory we pasted in, COPY the CSV name
os.listdir(data_dir)

# %%
# 8. Feel free to alter the variable name. Paste in CSV name from step 7 after "f'{data_dir}/"
weather_df = pandas.read_csv(f'{data_dir}/1. Weather Data.csv')
weather_df

# %%



