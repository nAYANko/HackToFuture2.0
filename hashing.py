import csv
import hashlib

encrp_data = [['-122.730000', '38.460000'], ['-117.060000', '32.760000'], ['-120.710000', '35.500000'], ['-118.310000', '34.050000'], ['-119.700000', '36.750000']]
for row in encrp_data:
    hashed_value = list(hashlib.sha256(str(row).encode()).hexdigest())
    print (hashed_value)
encrp_data = hashed_value   
print (encrp_data)
