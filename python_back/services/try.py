import os
import pandas as pd

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'dataset_manage', 'datasets', 'train_data_laptops.csv')
train = pd.read_csv(file_path, sep = ",")
X = train["text"]
y = train["rating"]