import sys
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# This is the initial csv file that stores the data
def read():
    with open("C:\\Users\\hp\\Desktop\\hack\\california_housing_test - Copy.csv", "r") as csvfile:
     reader = csv.reader(csvfile)
     data = list(reader)
    print (data)
    return(data)
def encrp(data,private_index):
    data_to_encrp = [[sublist[:2] for sublist in data]]
    #print(data_to_encrp)
    #print(sys.getsizeof(data_to_encrp))
    return(data_to_encrp)


data=read()
private_index=eval(input("enter list of indexes to be encrypted"))
data_to_encrp=encrp(data,private_index)

# This is a RSA encryption for anonymization of useless data
import base64
import hashlib

from Crypto.Cipher import AES  # from pycryptodomex v-3.10.4
from Crypto.Random import get_random_bytes

HASH_NAME = "SHA512"
IV_LENGTH = 12
ITERATION_COUNT = 65535
KEY_LENGTH = 32
SALT_LENGTH = 16
TAG_LENGTH = 16

def encrypt(password, plain_message):
    salt = get_random_bytes(SALT_LENGTH)     
    iv = get_random_bytes(IV_LENGTH)

    secret = get_secret_key(password, salt)

    cipher = AES.new(secret, AES.MODE_GCM, iv)

    encrypted_message_byte, tag = cipher.encrypt_and_digest(
        plain_message.encode("utf-8")
    )
    cipher_byte = salt + iv + encrypted_message_byte + tag

    encoded_cipher_byte = base64.b64encode(cipher_byte)
    return bytes.decode(encoded_cipher_byte)

def get_secret_key(password, salt):
    return hashlib.pbkdf2_hmac(
        HASH_NAME, password.encode(), salt, ITERATION_COUNT, KEY_LENGTH
    )

outputFormat = "{:<25}:{}"
secret_key = "B374A26A71490437AA024E4FADD5B497FDFF1A8EA6FF12F6FB65AF2720B59CCF"
plain_text = str(data_to_encrp)

#print("------ AES-GCM Encryption ------")
cipher_text = encrypt(secret_key, plain_text)
#print (cipher_text)
encrp_data = list(cipher_text)
#print (encrp_data)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2046, e=65535)
priv_key = key.exportKey("PEM")
public_key = key.publickey().exportKey("PEM")

key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(key)
keygone =list(cipher.encrypt(secret_key.encode("utf-8")))
#print ("Encrypted rsa key")
#print (keygone)

import hashlib

#for row in encrp_data:
   # encrp_data = list(hashlib.sha256(str(row).encode()).hexdigest())  
#print ("after hashing")
#print (encrp_data)


#ML model   
for i in data:
     del i[:2]
print(data)
df=list(data)
with open('proj.csv', mode ='w') as file:
    write=csv.writer(file)
    write.writerows(df)
df=pd.read_csv("C:\\Users\\hp\\Desktop\\hack\\proj.csv")
y=df['median_house_value']
x=df.drop('median_house_value', axis=1)
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
