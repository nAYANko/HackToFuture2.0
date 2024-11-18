from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#### Generate the public and private keys ####
key = RSA.generate(1024, e=65537)
priv_key = key.exportKey("PEM")
public_key = key.publickey().exportKey("PEM")
 


#list = [first_name, last_name, id]
list = ['Bob', 'Dylan', '15898']
listEncrypted = []

#Now let's encrypt the list with a public key
list_length = len(list)

for index in range(list_length-1):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(list[index])
    listEncrypted.append(ciphertext)