from sklearn.datasets import load_iris
import pandas as pd
data=load_iris(as_frame=True)
data.frame.to_csv('iris.csv',index=False)
