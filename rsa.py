from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(1024, e=65537)
priv_key = key.exportKey("PEM")
public_key = key.publickey().exportKey("PEM")

key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(text.encode("utf-8"))
print(text, ciphertext)