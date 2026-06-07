import hashlib, base64, urllib.parse, math, secrets, string
from cryptography.fernet import Fernet
from Crypto.Cipher import AES, DES, DES3, Blowfish
from Crypto.Util.Padding import pad

# मास्टर कीज
FERNET_KEY = b'uV9v_IqN_z8O5GmxYxUXFfOsh8G5Bv0D1zV29U4bK6E='
fernet_suite = Fernet(FERNET_KEY)
A_K, D_K, D3_K, B_K = b'SixteenByteKey16', b'8ByteKey', b'TwentyFourByteKey24Bytes', b'BlowfishKeyMustBeLong'

# १. स्ट्रेंथ चेक
def check_strength(t):
    if len(t) < 6: return 20
    score = sum([len(t) >= 10, any(c.isupper() for c in t), any(c.isdigit() for c in t), any(not c.isalnum() for c in t)]) * 20
    return min(score, 100)

# २. Brute-Force अटॅक टाइम कॅल्क्युलेटर
def get_attack_time(password):
    length = len(password)
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32
    
    combinations = math.pow(charset, length) if charset > 0 else 1
    pc_speed = 100_000_000
    super_speed = 100_000_000_000
    
    def format_time(seconds):
        if seconds < 1: return "Instant"
        if seconds < 60: return f"{seconds:.2f} Sec"
        if seconds < 3600: return f"{seconds/60:.2f} Min"
        if seconds < 86400: return f"{seconds/3600:.2f} Hrs"
        if seconds < 31536000: return f"{seconds/86400:.2f} Days"
        return f"{seconds/31536000:.2f} Years"
    return format_time(combinations / pc_speed), format_time(combinations / super_speed)

# ३. १५ अटॅक वेक्टर्सचे विश्लेषण
def get_detailed_attack_analysis(password):
    pc_t, super_t = get_attack_time(password)
    return {
        "Brute Force": pc_t,
        "Dictionary Attack": "10x Faster",
        "Rainbow Table": "Instant (If Hash found)",
        "Social Engineering": "Human Factor",
        "Credential Stuffing": "Dependent on DB",
        "DDoS": "N/A (Service Denial)",
        "Man-in-the-Middle": "Intercept Dependent",
        "Side-Channel Attack": "Requires Hardware",
        "Quantum Brute Force": "Seconds (Future Tech)",
        "Dictionary Hybrid": "5x Faster",
        "Mask Attack": "Variable Speed",
        "Rule-Based Attack": "Depends on Dictionary",
        "Permutation Attack": "Variable",
        "Phishing": "Instant",
        "Offline Rainbow": "Instant"
    }

# ४. नवीन फिचर: Salt Generator
def generate_salt(length=16):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# ५. नवीन फिचर: Payload Entropy (डेटा रँडमनेस)
def get_entropy(t):
    return len(t) * 8 # Bit length as simple entropy proxy

# ६. नवीन फिचर: Steganography (Binary Hidden Format)
def hide_text_in_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# ७. नवीन फिचर: Key Validator
def validate_custom_key(key):
    return len(key) >= 12 and any(c.isupper() for c in key) and any(c.isdigit() for c in key)

# एन्क्रिप्शन इंजिन
def run_encrypt(t, algo):
    try:
        if algo == 'caesar': return "".join(chr((ord(c) - (65 if c.isupper() else 97) + 4) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in t)
        elif algo == 'reverse': return t[::-1]
        elif algo == 'base64': return base64.b64encode(t.encode()).decode()
        elif algo == 'base32': return base64.b32encode(t.encode()).decode()
        elif algo == 'hex': return t.encode().hex()
        elif algo == 'url': return urllib.parse.quote(t)
        elif algo == 'md5': return hashlib.md5(t.encode()).hexdigest()
        elif algo == 'sha1': return hashlib.sha1(t.encode()).hexdigest()
        elif algo == 'sha256': return hashlib.sha256(t.encode()).hexdigest()
        elif algo == 'sha512': return hashlib.sha512(t.encode()).hexdigest()
        elif algo == 'fernet': return fernet_suite.encrypt(t.encode()).decode()
        elif algo == 'aes': return base64.b64encode(AES.new(A_K, AES.MODE_ECB).encrypt(pad(t.encode(), 16))).decode()
        elif algo == 'des': return base64.b64encode(DES.new(D_K, DES.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()
        elif algo == '3des': return base64.b64encode(DES3.new(D3_K, DES3.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()
        elif algo == 'blowfish': return base64.b64encode(Blowfish.new(B_K, Blowfish.MODE_ECB).encrypt(pad(t.encode(), 8))).decode()
    except: return "Error: Encryption Failed"
    return "Unknown Scheme"

# --- Decryption Engine ---
def run_decrypt(t, algo):
    try:
        if algo == 'caesar': 
            return "".join(chr((ord(c) - (65 if c.isupper() else 97) - 4) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in t)
        elif algo == 'reverse': 
            return t[::-1]
        elif algo == 'base64': 
            return base64.b64decode(t.encode()).decode()
        elif algo == 'base32': 
            return base64.b32decode(t.encode()).decode()
        elif algo == 'hex': 
            return bytes.fromhex(t).decode()
        elif algo == 'url': 
            return urllib.parse.unquote(t)
        elif algo == 'fernet': 
            return fernet_suite.decrypt(t.encode()).decode()
        elif algo == 'aes': 
            cipher = AES.new(A_K, AES.MODE_ECB)
            return cipher.decrypt(base64.b64decode(t)).decode().strip()
        elif algo == 'des': 
            cipher = DES.new(D_K, DES.MODE_ECB)
            return cipher.decrypt(base64.b64decode(t)).decode().strip()
        elif algo == '3des': 
            cipher = DES3.new(D3_K, DES3.MODE_ECB)
            return cipher.decrypt(base64.b64decode(t)).decode().strip()
        elif algo == 'blowfish': 
            cipher = Blowfish.new(B_K, Blowfish.MODE_ECB)
            return cipher.decrypt(base64.b64decode(t)).decode().strip()
        elif algo in ['md5', 'sha1', 'sha256', 'sha512']:
            return "❌ Hashing is a one-way process. Cannot be decrypted."
    except Exception as e:
        return f"Error: Decryption Failed ({str(e)})"
    return "Unknown Scheme"