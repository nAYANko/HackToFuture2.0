import hashlib
import secrets
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'Name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 'alice.johnson@example.com'],
    'Phone': ['123-456-7890', '456-789-0123', '789-012-3456']
})

# 1. Data Encryption
# In this example, we'll use a simple XOR encryption for demonstration purposes
def encrypt_data(data):
    key = 'secretkey'
    encrypted_data = []
    for value in data:
        encrypted_value = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(value))
        encrypted_data.append(encrypted_value)
    return encrypted_data

# Encrypt PII columns (Name, Email, Phone)
data['Name'] = encrypt_data(data['Name'])
data['Email'] = encrypt_data(data['Email'])
data['Phone'] = encrypt_data(data['Phone'])

# 2. Pseudonymization
# Replace real names with unique pseudonyms
data['Pseudonym'] = ['user_' + str(i) for i in range(len(data))]

# 3. Hashing
# Apply hash functions to sensitive data
def hash_data(data):
    return [hashlib.sha256(value.encode()).hexdigest() for value in data]

data['Email'] = hash_data(data['Email'])
data['Phone'] = hash_data(data['Phone'])

# 4. Tokenization
# Replace sensitive data with randomly generated tokens
def generate_token():
    return secrets.token_hex(16)

data['Email'] = [generate_token() for _ in range(len(data))]
data['Phone'] = [generate_token() for _ in range(len(data))]

# 5. Aggregate Data - This can be done based on specific business requirements

# 6. Data Masking
# Mask specific parts of the data
data['Phone'] = data['Phone'].apply(lambda x: x[:-4] + 'XXXX')

# 7. K-Anonymity - This can be achieved by grouping similar records together

# 8. Differential Privacy - Add noise to the data (not implemented in this example)

# 9. Secure Access Controls - Implement access controls based on user roles and permissions

# 10. Regular Audits - Perform periodic audits to ensure data anonymization techniques are effective

# 11. Informed Consent - Obtain explicit consent from individuals before using their data

# 12. Educate Personnel - Provide training on privacy and ethical considerations

print(data)
