from theme_styles import COMMON_CSS
def get_page():
    return f"""<html><head><title>Page 3 - Encoders</title>{COMMON_CSS}</head><body><div class="container">
    <h2>Page 3: Encoding Workspace</h2><form method="POST"><label>Enter Plain Text:</label><textarea name="text" rows="2" required></textarea>
    <label>Select Encoding Scheme:</label><select name="algo"><option value="base64">Base64</option><option value="base32">Base32</option><option value="hex">Hex Encoder</option><option value="url">URL Percent</option></select>
    <button type="submit">Encode Payload</button></form><a href="/dashboard" class="btn" style="background:#333;">← Back to Control Panel</a></div></body></html>"""