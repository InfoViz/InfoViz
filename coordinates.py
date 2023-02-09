import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\User\Downloads\queryResults (3).csv")

df.head()

BBox = (df.longitude.min(-1.586425),   df.longitude.max(1.529006),      
         df.latitude.min(58.465533), df.latitude.max(49.967849))
