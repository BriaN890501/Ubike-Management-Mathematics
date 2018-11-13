#Importing libraries
import numpy as np
import pandas as pd
import linear as l
import matplotlib.pyplot as plt

#Read training input
df = pd.read_csv('temp_cnt_train.csv')
df.columns=['temp','cnt']
temp=np.array(df.loc[:, "temp"])
cnt=np.array(df.loc[:, "cnt"])
data = pd.DataFrame(np.column_stack([temp,cnt]),columns=['x','y'])
plt.plot(data['x'],data['y'],'.')
# plt.show()
for i in range(2,16):  #power of 1 is already there
    colname = 'x_%d'%i      #new var will be x_power
    data[colname] = data['x']**i

task=input("train, validate or test?\n")
#------------------------------Linear----------------------------------
#Initialize a dataframe to store the results:
col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
ind = ['model_pow_%d'%i for i in range(1,16)]
coef_matrix_simple = pd.DataFrame(index=ind, columns=col)

#Iterate through all powers and assimilate results
for i in range(1,16):
    coef_matrix_simple.iloc[i-1,0:i+2] = l.linear_regression_train(data, power=i)

#Set the display format to be scientific for ease of analysis
pd.options.display.float_format = '{:,.2g}'.format
pickt=coef_matrix_simple['rss'].idxmin()
if task=="train":
	print(coef_matrix_simple)
	print('------------------------')
	print(coef_matrix_simple['rss'])
	print('------------------------\nmodel with min rss:')
	print(pickt, '{:,.2g}'.format(coef_matrix_simple['rss'].min()))

#Validation
df = pd.read_csv('temp_cnt_valid.csv')
df.columns=['temp','cnt']
temp=np.array(df.loc[:, "temp"])
cnt=np.array(df.loc[:, "cnt"])
data = pd.DataFrame(np.column_stack([temp,cnt]),columns=['x','y'])
for i in range(2,16):  #power of 1 is already there
    colname = 'x_%d'%i      #new var will be x_power
    data[colname] = data['x']**i

for i in range(1,16):
	coef_matrix_simple.iloc[i-1,0:i+2] = l.linear_regression_valid(data, power=i)
pickv=coef_matrix_simple['rss'].idxmin()
if task=="validate":
	print(coef_matrix_simple['rss'])
	print('------------------------\nmodel with min rss:')
	print(pickv, '{:,.2g}'.format(coef_matrix_simple['rss'].min()))

#Test
df = pd.read_csv('temp_cnt_test.csv')
df.columns=['temp','cnt']
temp=np.array(df.loc[:, "temp"])
cnt=np.array(df.loc[:, "cnt"])
data = pd.DataFrame(np.column_stack([temp,cnt]),columns=['x','y'])
for i in range(2,16):  #power of 1 is already there
    colname = 'x_%d'%i      #new var will be x_power
    data[colname] = data['x']**i

for i in range(1,16):
	coef_matrix_simple.iloc[i-1,0:i+2] = l.linear_regression_valid(data, power=i)
pick=coef_matrix_simple['rss'].idxmin()
if task=="test":
	print(coef_matrix_simple['rss'])
	print('------------------------\nmodel with min rss:')
	print(pick, '{:,.2g}'.format(coef_matrix_simple['rss'].min()))
	print('------------------------\nmodel picked by training data:\n%s' %coef_matrix_simple.loc[[pickt]]['rss'])
	print('------------------------\nmodel picked by validation data:\n%s' %coef_matrix_simple.loc[[pickv]]['rss'])

