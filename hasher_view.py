from theme_styles import COMMON_CSS
def get_page():
    return f"""<html><head><title>Page 4 - Hashers</title>{COMMON_CSS}</head><body><div class="container">
    <h2>Page 4: Secure Hashing (One-Way)</h2><form method="POST"><label>Enter Text to Hash:</label><textarea name="text" rows="2" required></textarea>
    <label>Select Hash Algorithm:</label><select name="algo"><option value="md5">MD5</option><option value="sha1">SHA-1</option><option value="sha256">SHA-256</option><option value="sha512">SHA-512</option></select>
    <button type="submit">Generate Cryptographic Hash</button></form><a href="/dashboard" class="btn" style="background:#333;">← Back to Control Panel</a></div></body></html>"""