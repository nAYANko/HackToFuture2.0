import pandas as pd
import csv 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# This is the initial csv file that stores the data
def read():
    data_=pd.read_csv("C:\\Users\\hp\\Desktop\\hack\\california_housing_test - Copy.csv")
    data=list(data_)
    return(data)
def encrp(data,private_index):
    data_to_encrp=[[0]*len(data[0])]*len(data)
    for i in range(len(data)):
        for j in (private_index):
            data_to_encrp[i][j]=data[i][j]
    return(data_to_encrp)
def superimpose(data,encrp_data,private_index):
    for i in range(len(data)):
        for j in (private_index):
            final_data[i][j]=encrp_data[i][j]
    return(final_data)
data=read()
private_index=eval(input("enter list of indexes to be encrypted"))
data_to_encrp=encrp(data,private_index)

# This is a RSA encryption for anonymization of useless data
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(1024, e=65537)
priv_key = key.exportKey("PEM")
public_key = key.publickey().exportKey("PEM")

key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(key)
encrp_data = [[0]*len(data_to_encrp[0])]*len(data_to_encrp)
for i in range(len(data_to_encrp)):
    encrp_data[i] =list(cipher.encrypt(str(data_to_encrp[i]).encode("utf-8")))
final_data=superimpose(data,encrp_data,private_index)


df=list(final_data)
for i in (df[2:]):
    print("the parameter is: ",i)
    y=df[i]
    x=df.drop(i, axis=1)
    x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=100)
    lr= LinearRegression()
    lr.fit(x_train,y_train)
    y_lr_train_pred=lr.predict(x_train)
    y_lr_test_pred=lr.predict(x_test)
    lr_train_mse= mean_squared_error(y_train,y_lr_train_pred)
    lr_train_r2=r2_score(y_train,y_lr_train_pred)
    lr_test_mse= mean_squared_error(y_test,y_lr_test_pred)
    lr_test_r2=r2_score(y_test,y_lr_test_pred)
    lr_results= pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
    lr_results.columns= ['Method','Training MSE','Training R2','Test MSE','Test R2']
    print(lr_results)
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