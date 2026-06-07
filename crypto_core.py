import hashlib, base64, urllib.parse
from cryptography.fernet import Fernet
from Crypto.Cipher import AES, DES, DES3, Blowfish
from Crypto.Util.Padding import pad

FERNET_KEY = b'uV9v_IqN_z8O5GmxYxUXFfOsh8G5Bv0D1zV29U4bK6E='
fernet_suite = Fernet(FERNET_KEY)
AES_KEY, DES_KEY, DES3_KEY, BLOWFISH_KEY = b'SixteenByteKey16', b'8ByteKey', b'TwentyFourByteKey24Bytes', b'BlowfishKeyMustBeLong'

def algo_caesar(t): return "".join(chr((ord(c) - (65 if c.isupper() else 97) + 4) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in t)
def algo_reverse(t): return t[::-1]
def algo_base64(t): return base64.b64encode(t.encode()).decode()
def algo_base32(t): return base64.b32encode(t.encode()).decode()
def algo_hex(t): return t.encode().hex()
def algo_url(t): return urllib.parse.quote(t)
def algo_md5(t): return hashlib.md5(t.encode()).hexdigest()
def algo_sha1(t): return hashlib.sha1(t.encode()).hexdigest()
def algo_sha256(t): return hashlib.sha256(t.encode()).hexdigest()
def algo_sha512(t): return hashlib.sha512(t.encode()).hexdigest()
def algo_fernet(t): return fernet_suite.encrypt(t.encode()).decode()
def algo_aes(t): return base64.b64encode(AES.new(AES_KEY, AES.MODE_ECB).encrypt(pad(t.encode(), 16))).decode()
def algo_des(t): return base64.b64encode(DES.new(DES_KEY, DES.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()
def algo_3des(t): return base64.b64encode(DES3.new(DES3_KEY, DES3.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()
def algo_blowfish(t): return base64.b64encode(Blowfish.new(BLOWFISH_KEY, Blowfish.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()