# """
#  Dataset is downloaded from given link:
#     https://www.kaggle.com/datasets/zaraavagyan/weathercsv/download?datasetVersionNumber=1 
# """

# #Import libraries

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# #Load and Read Dataset
# data=pd.read_csv("/home/hacquees/Downloads/archive/weather.csv")
# print(data.head(10))

# #Dimensions of the dataframe

# print(data.shape)

# #Datatypes of the dataframe

# print(data.dtypes)

# #Statistical details of the dataframe
# print(data.describe())

# #Counting for missing values in each columns
# print(data.isnull().sum())

# #Number of Distinct Observation
# print(data.nunique())

# #Data Analysis
# sns.set_style("darkgrid")
# sns.regplot(data=data, x="Temp3pm", y="Humidity3pm", color="g")
# plt.title("Relation between Temp3pm and Humidity3pm")
# plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
# plt.show()

# #varition of rainfall with temperature at 3pm 
# plt.figure(figsize=(14,6))
# sns.lineplot(data =[ data['Rainfall'],data["Temp3pm"]])
# plt.xlabel('Temp3pm')
# plt.title("Varition of humidity at 9am with temperature at 9am ")
# plt.savefig('fig2.png', dpi=400, bbox_inches='tight')
# plt.show()

# #MinTemp 
# plt.stackplot(data["Temp9am"],data["Temp3pm"],data["Rainfall"],labels=['Temp9am','Temp3pm','Rainfall'])
# plt.legend()
# plt.savefig('fig3.png', dpi=400, bbox_inches='tight')
# plt.show()

# plt.bar(data["Rainfall"],data["MinTemp"],width=0.8,color='r',label='MinTemp',align='edge')
# plt.bar(data['Rainfall'],data["MaxTemp"],bottom=data['MinTemp'],width=0.8,color='b',label='MaxTemp',align='edge')
# plt.legend()
# plt.savefig('fig4.png', dpi=400, bbox_inches='tight')
# plt.show()


# # Humidity9am plot     
# # Humidity3pm plot       
# # Pressure9am plot    
# # Pressure3pm plot

# plt.subplot(2,2,2)
# interval = [0,10,20,30,40,50]
# plt.plot(data["Humidity9am"])

# plt.xlabel("Humidity9am")
# plt.subplot(2,2,1)
# interval = [0,10,20,30,40,50]
# plt.plot(data["Humidity3pm"])

# plt.xlabel("Humidity3pm")
# plt.subplot(2,2,3)
# plt.subplots_adjust(hspace=1,wspace=1)

# plt.plot(data["Pressure9am"])

# plt.xlabel("Pressure9am")
# plt.subplot(2,2,4)

# interval = [0,10,20,30,40,50]
# plt.plot(data["Pressure3pm"])

# plt.xlabel("Pressure3pm")
# plt.savefig('fig5.png', dpi=400, bbox_inches='tight')

# plt.show()
import pandas as pd

import numpy as np

from pandas import *



frame3 = pd.DataFrame([[6, np.nan, 6],[np.nan, np.nan, np.nan], [2, np.nan, 5]],index = ['blue', 'green', 'red'],columns=['ball', 'mug', 'pen'])

print (frame3. dropna (how='all'))