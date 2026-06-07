import base64, urllib.parse, re
# 👇 हे ३ इम्पोर्ट्स असणे अनिवार्य आहे, अन्यथा Fernet ओळखणार नाही
from cryptography.fernet import Fernet 
from Crypto.Cipher import AES, DES, DES3, Blowfish
from Crypto.Util.Padding import unpad

# आता याच्या खाली तुझा FERNET_KEY आणि बाकीचा कोड लिही...
FERNET_KEY = b'uV9v_IqN_z8O5GmxYxUXFfOsh8G5Bv0D1zV29U4bK6E='
fernet_suite = Fernet(FERNET_KEY)
# ... बाकी कोड
A_K, D_K, D3_K, B_K = b'SixteenByteKey16', b'8ByteKey', b'TwentyFourByteKey24Bytes', b'BlowfishKeyMustBeLong'

def get_algo_time_complexity(algo_key):
    """
    प्रत्येक वेगवेगळ्या अल्गोरिदमला क्रॅक करण्यासाठी लागणारा डिफरेंशियल वेळ
    """
    time_matrix = {
        'caesar': ("0.001 Seconds", "0.000001 Seconds (Instant)"),
        'reverse': ("0.001 Seconds", "Instant"),
        'base64': ("0.001 Seconds (No Key)", "Instant (Encoding Only)"),
        'base32': ("0.001 Seconds (No Key)", "Instant (Encoding Only)"),
        'hex': ("0.001 Seconds (No Key)", "Instant (Encoding Only)"),
        'url': ("0.001 Seconds (No Key)", "Instant (Encoding Only)"),
        'des': ("2.1 Hours (56-bit Key)", "1.2 Seconds (ASIC Rig)"),
        'blowfish': ("8.4 x 10^32 Years", "2.1 x 10^24 Years"),
        '3des': ("4.2 x 10^21 Years", "1.5 x 10^12 Years"),
        'aes': ("3.4 x 10^38 Years (Unbreakable)", "5.2 x 10^28 Years"),
        'fernet': ("3.4 x 10^38 Years (Unbreakable)", "5.2 x 10^28 Years"),
        'md5': ("Instant (Rainbow Tables)", "0.0001 Seconds (GPU Array)"),
        'sha1': ("45 Days (Collisions)", "12 Minutes (High-End Rig)"),
        'sha256': ("1.1 x 10^63 Years", "9.8 x 10^51 Years"),
        'sha512': ("2.8 x 10^140 Years", "3.4 x 10^128 Years")
    }
    return time_matrix.get(algo_key, ("Unknown", "Unknown"))

def decrypt_single(t_stripped, algo):
    try:
        if algo == 'caesar':
            return "".join(chr((ord(c) - (65 if c.isupper() else 97) - 4) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in t_stripped)
        elif algo == 'reverse':
            return t_stripped[::-1]
        elif algo == 'base64':
            return base64.b64decode(t_stripped.encode()).decode('utf-8', errors='ignore')
        elif algo == 'base32':
            return base64.b32decode(t_stripped.encode()).decode('utf-8', errors='ignore')
        elif algo == 'hex':
            return bytes.fromhex(t_stripped).decode('utf-8', errors='ignore')
        elif algo == 'url':
            return urllib.parse.unquote(t_stripped)
        elif algo == 'fernet':
            return fernet_suite.decrypt(t_stripped.encode()).decode()
        elif algo == 'aes':
            return unpad(AES.new(A_K, AES.MODE_ECB).decrypt(base64.b64decode(t_stripped)), 16).decode()
        elif algo == 'des':
            return unpad(DES.new(D_K, DES.MODE_ECB).decrypt(base64.b64decode(t_stripped)), 8).decode()
        elif algo == '3des':
            return unpad(DES3.new(D3_K, DES3.MODE_ECB).decrypt(base64.b64decode(t_stripped)), 8).decode()
        elif algo == 'blowfish':
            return unpad(Blowfish.new(B_K, Blowfish.MODE_ECB).decrypt(base64.b64decode(t_stripped)), 8).decode()
        elif algo in ['md5', 'sha1', 'sha256', 'sha512']:
            return "🛡️ Hash Integrity Lock (One-Way Function - Cannot Decrypt)"
    except:
        return "❌ Decryption Mismatch / Bad Token Structure"
    return "Unknown Scheme"

def run_matrix_decryption(t):
    t_stripped = t.strip()
    algos = {
        'caesar': 'Caesar Shift Cipher', 'reverse': 'Reverse String Cipher',
        'fernet': 'Fernet Private Token', 'aes': 'AES-256 Decryption',
        'des': 'DES Block Legacy', '3des': 'Triple DES (3DES)', 'blowfish': 'Blowfish Plain Cipher',
        'base64': 'Base64 Decoder', 'base32': 'Base32 Decoder', 'hex': 'Hexadecimal to Plain', 'url': 'URL Percent Decoder',
        'md5': 'MD5 Hash', 'sha1': 'SHA-1 Hash', 'sha256': 'SHA-256 Bit Hash', 'sha512': 'SHA-512 Bit Hash'
    }
    results = {}
    for key, name in algos.items():
        pc_time, super_time = get_algo_time_complexity(key)
        out = decrypt_single(t_stripped, key)
        # आउटपुट सोबत दोन्ही मशीनचा वेळ मॅप करून पाठवणे
        results[name] = {
            'output': out,
            'pc_time': pc_time,
            'super_time': super_time
        }
    return results
def get_brute_force_stats(algo):
    stats = {
        'des': ("56-bit", "7.2 x 10^16 combinations"),
        'aes': ("256-bit", "1.1 x 10^77 combinations"),
        'md5': ("128-bit", "3.4 x 10^38 combinations"),
        'sha256': ("256-bit", "1.1 x 10^77 combinations")
    }
    return stats.get(algo, ("Unknown", "N/A"))