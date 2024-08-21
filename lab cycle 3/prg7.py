print("SJC23MCA-2009 : AKSHAY UNNI M V\n Batch : MCA 2022-24")
import pandas as pd
df = pd.read_csv('IRIS.csv')
print("Shape of the dataset is : ",df.shape)
print("First 5 and last five rows of data set\n",df)
print("Size of dataset : ",df.size)
print("No. of samples available for each variety\n",df.count())
print("Description of the data set\n",df.describe())