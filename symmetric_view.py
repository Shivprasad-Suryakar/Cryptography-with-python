from theme_styles import COMMON_CSS
def get_page():
    return f"""<html><head><title>Page 5 - Ciphers</title>{COMMON_CSS}</head><body><div class="container">
    <h2>Page 5: Symmetric Crypto Shield</h2><form method="POST"><label>Enter Secret Message:</label><textarea name="text" rows="2" required></textarea>
    <label>Select Cipher Method:</label><select name="algo"><option value="caesar">Caesar Cipher</option><option value="reverse">Reverse Cipher</option><option value="fernet">Fernet (AES-128)</option><option value="aes">AES-256 Standard</option><option value="des">DES Legacy</option><option value="3des">Triple DES</option><option value="blowfish">Blowfish</option></select>
    <button type="submit">Run Cipher Algorithm</button></form><a href="/dashboard" class="btn" style="background:#333;">← Back to Control Panel</a></div></body></html>"""