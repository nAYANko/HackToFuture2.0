import csv
# This is the initial csv file that stores the data
def read():
    with open('C:\\Users\\hp\\Desktop\\hack\\california_housing_test - Copy.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        data=list(csvFile)
    return(data)
data_to_encrp = []
def encrp(data,private_index):
    for i in range(len(data)):
        for j in (private_index):
            data_to_encrp[i][j]=data[i][j]
    return(data_to_encrp)
def superimpose(data,encrp_data,private_index):
    for i in range(len(data)):
        for j in (private_index):
            final_data[i][j]=encrp_data[i][j]
    return(final_data)
#def write():
    with open('xyz.csv', 'a') as f:
        n=input("do u want to enter more data? y/n")
        writer=csv.writer(f)
        while(n!="n"):
            row=eval(input("enter row"))
#write()
data=read()
private_index=eval(input("enter list of indexes to be encrypted:"))
data_to_encrp=encrp(data,private_index)
print (data_to_encrp)

# This is a RSA encryption for anonymization of useless data
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(1024, e=65537)
priv_key = key.exportKey("PEM")
public_key = key.publickey().exportKey("PEM")

key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(key)
encrp_data = cipher.encrypt(data_to_encrp.encode("utf-8"))

import pandas as pd
df=pd.read_csv("C:\\Users\\hp\\Desktop\\hack\\california_housing_test - Copy.csv")
y=df['median_house_value']
x=df.drop('median_house_value', axis=1)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=100)
from sklearn.linear_model import LinearRegression
lr= LinearRegression()
lr.fit(x_train,y_train)
y_lr_train_pred=lr.predict(x_train)
y_lr_test_pred=lr.predict(x_test)
from sklearn.metrics import mean_squared_error, r2_score
lr_train_mse= mean_squared_error(y_train,y_lr_train_pred)
lr_train_r2=r2_score(y_train,y_lr_train_pred)
lr_test_mse= mean_squared_error(y_test,y_lr_test_pred)
lr_test_r2=r2_score(y_test,y_lr_test_pred)
lr_results= pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns= ['Method','Training MSE','Training R2','Test MSE','Test R2']
print(lr_results)
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train,y_train)
y_rf_train_pred=rf.predict(x_train)
y_rf_test_pred=rf.predict(x_test)
rf_train_mse= mean_squared_error(y_train,y_rf_train_pred)
rf_train_r2=r2_score(y_train,y_rf_train_pred)
rf_test_mse= mean_squared_error(y_test,y_rf_test_pred)
rf_test_r2=r2_score(y_test,y_rf_test_pred)
rf_results= pd.DataFrame(['Random forest',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
rf_results.columns= ['Method','Training MSE','Training R2','Test MSE','Test R2']
print(rf_results)