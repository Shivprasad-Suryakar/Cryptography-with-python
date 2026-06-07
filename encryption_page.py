def get_page():
    return f"""
    <html>
    <head>
        <style>
            /* CSS स्टाईल्स फक्त इथेच असतील */
            body {{
                background: #050505;
                background-image: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #000 100%);
                color: #fff;
                font-family: 'Inter', 'Segoe UI', sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
            }}

            h2 {{
                color: #00d2ff;
                font-size: 2rem;
                text-transform: uppercase;
                letter-spacing: 4px;
                margin-bottom: 40px;
                text-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
            }}

            form {{
                background: rgba(20, 20, 20, 0.7);
                backdrop-filter: blur(15px);
                padding: 50px;
                border-radius: 25px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
                width: 450px;
            }}

            textarea, select {{
                width: 100%;
                padding: 18px;
                margin: 15px 0;
                background: rgba(0, 0, 0, 0.4);
                border: 1px solid #333;
                color: #fff;
                border-radius: 12px;
            }}

            button {{
                width: 100%;
                padding: 18px;
                margin-top: 10px;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                border: none;
                border-radius: 12px;
                color: #fff;
                font-weight: bold;
                cursor: pointer;
            }}
        </style>
        
    </head>
    <body>
        </div>
        <h2>🔐 Cryptographic Workspace 🛡️</h2>
        <form method="POST" action="/encryption">
            <textarea id="text" name="text" rows="5" placeholder="✏️ Enter plaintext here..." required></textarea>
            
            <div id="strength-meter"></div>
            
            <select name="algo" required>
                <option value="" disabled selected>⚙️ -- Select Algorithm --</option>
                <option value="aes">AES-256 🔒</option>
                <option value="des">DES 🔑</option>
                <option value="3des">3DES 🔐</option>
                <option value="blowfish">Blowfish 🐡</option>
                <option value="fernet">Fernet 🧪</option>
                <option value="md5">MD5 ⚡</option>
                <option value="sha1">SHA-1 🛡️</option>
                <option value="sha256">SHA-256 💠</option>
                <option value="sha512">SHA-512 💎</option>
                <option value="base64">Base64 📦</option>
                <option value="base32">Base32 📦</option>
                <option value="hex">Hexadecimal 🔢</option>
                <option value="caesar">Caesar Cipher 🏛️</option>
                <option value="reverse">Reverse String 🔄</option>
                <option value="url">URL Encoding 🌐</option>
            </select>
            
            <button type="submit">🚀 Execute Encryption</button>
        </form>

        <script>
            const textarea = document.getElementById('text');
            const meter = document.getElementById('strength-meter');

            textarea.addEventListener('input', function() {{
                const val = this.value;
                if(val.length === 0) {{ meter.innerText = ""; return; }}
                
                if(val.length < 5) {{ 
                    meter.innerText = "Weak 🔴"; meter.style.color = "#ff4d4d"; 
                }} else if(val.length < 10) {{ 
                    meter.innerText = "Medium 🟡"; meter.style.color = "#ffa500"; 
                }} else {{ 
                    meter.innerText = "Strong 🟢"; meter.style.color = "#00ff00"; 
                }}
            }});
        </script>
    </body>
    </html>
    """