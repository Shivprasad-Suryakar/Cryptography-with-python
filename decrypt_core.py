import base64
from cryptography.fernet import Fernet
from Crypto.Cipher import AES, DES, DES3, Blowfish
from Crypto.Util.Padding import unpad

FERNET_KEY = b'uV9v_IqN_z8O5GmxYxUXFfOsh8G5Bv0D1zV29U4bK6E='
fernet_suite = Fernet(FERNET_KEY)
AES_KEY, DES_KEY, DES3_KEY, BLOWFISH_KEY = b'SixteenByteKey16', b'8ByteKey', b'TwentyFourByteKey24Bytes', b'BlowfishKeyMustBeLong'

def dec_caesar(t): return "".join(chr((ord(c) - (65 if c.isupper() else 97) - 4) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in t)
def dec_reverse(t): return t[::-1]
def dec_base64(t):
    try: return base64.b64decode(t.encode()).decode()
    except: return "Error: Invalid Base64 Data"
def dec_fernet(t):
    try: return fernet_suite.decrypt(t.encode()).decode()
    except: return "Error: Invalid Fernet Token"
def dec_aes(t):
    try: return unpad(AES.new(AES_KEY, AES.MODE_ECB).decrypt(base64.b64decode(t.encode())), 16).decode()
    except: return "Error: AES Decryption Failed"