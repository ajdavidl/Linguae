
import pandas as pd
import numpy as np

print("Reading the mini.h5 file.")
# https://github.com/commonsense/conceptnet-numberbatch
df = pd.read_hdf("mini.h5")
print(df.info())

print("Converting the h5 file to a text file. This will create a large file: more than 12 GB.")
np.savetxt('conceptnetNumberbatchMini.vec', df.reset_index().values,
           delimiter=" ",
           header="{} {}".format(len(df), len(df.columns)),
           comments="",
           fmt=["%s"] + ["%.18e"]*len(df.columns))
