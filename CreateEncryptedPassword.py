import hashlib

integerLength = 5

def startEncryption():
  pwd = hashlib.pbkdf2_hmac('sha256', b"password", b"salt", 100000, dklen = integerLength)
  return pwd.hex()

if(__name__ == "__main__"):
  print(f"Here is your password encrypted: {startEncryption()}")
