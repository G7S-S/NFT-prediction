import pandas as pd
import numpy as np

df= pd.read_csv("nfts_train_withoutopenrarity.csv")

from sklearn.model_selection import GroupShuffleSplit

groups = df["collection_id"]
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in gss.split(df, groups=groups):
    train_df = df.iloc[train_index]
    test_df = df.iloc[test_index]

