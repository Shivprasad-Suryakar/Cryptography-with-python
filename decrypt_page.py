def get_page():
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #050505; color: #fff; font-family: 'Segoe UI', sans-serif; padding: 40px; }}
            .container {{ max-width: 600px; margin: auto; background: #111; padding: 30px; border-radius: 15px; border: 1px solid #333; }}
            textarea, select {{ width: 100%; padding: 15px; margin: 15px 0; background: #000; border: 1px solid #444; color: #00d2ff; border-radius: 8px; }}
            button {{ width: 100%; padding: 15px; background: linear-gradient(90deg, #00d2ff, #3a7bd5); border: none; border-radius: 8px; color: #fff; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/dashboard" style="color: #00d2ff; text-decoration: none;">&larr; Back to Dashboard</a>
            <h2>🔓 Decryption Workspace 🛡️</h2>
            <form method="POST" action="/decrypt">
                <textarea name="text" rows="5" placeholder="✏️ Enter ciphertext here..." required></textarea>
                <select name="algo" required>
                    <option value="" disabled selected>⚙️ -- Select Algorithm (15 Available) --</option>
                    <option value="all">✨ ALL - Simultaneous Decryption Matrix</option>
                    <option value="caesar">Caesar Shift</option>
                    <option value="reverse">Reverse String</option>
                    <option value="fernet">Fernet (AES-128)</option>
                    <option value="aes">AES-256</option>
                    <option value="des">DES Legacy</option>
                    <option value="3des">Triple DES</option>
                    <option value="blowfish">Blowfish</option>
                    <option value="base64">Base64 Decoder</option>
                    <option value="base32">Base32 Decoder</option>
                    <option value="hex">Hexadecimal</option>
                    <option value="url">URL Decoder</option>
                    <option value="md5">MD5 Hash</option>
                    <option value="sha1">SHA-1 Hash</option>
                    <option value="sha256">SHA-256</option>
                    <option value="sha512">SHA-512</option>
                </select>
                <button type="submit">🚀 Execute Decryption</button>
            </form>
        </div>
    </body>
    </html>
    """