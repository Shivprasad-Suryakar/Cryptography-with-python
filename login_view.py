from theme_styles import COMMON_CSS

def get_page(msg=""):
    return f"""<html>
<head>
    <title>Secure Login Portal</title>
    <style>
        body {{ 
            background: radial-gradient(circle at center, #1a1a1a, #050505); 
            height: 100vh; display: flex; align-items: center; justify-content: center; 
            font-family: 'Segoe UI', sans-serif; color: white;
            animation: fadeIn 1s ease-in;
        }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        .container {{ 
            background: rgba(20, 20, 20, 0.8); padding: 40px; border-radius: 15px; 
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.2); 
            border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);
            width: 100%; max-width: 400px;
        }}
        h2 {{ color: #00d2ff; text-align: center; text-transform: uppercase; letter-spacing: 2px; }}
        input {{ 
            width: 100%; padding: 12px; margin: 10px 0 20px; background: #000; 
            border: 1px solid #333; color: #00e676; border-radius: 5px; outline: none;
            transition: 0.4s;
        }}
        input:focus {{ border-color: #00d2ff; box-shadow: 0 0 10px rgba(0, 210, 255, 0.3); }}
        button {{ 
            width: 100%; padding: 12px; background: linear-gradient(90deg, #00d2ff, #00e676);
            border: none; border-radius: 5px; color: black; font-weight: bold; cursor: pointer;
            transition: 0.3s;
        }}
        button:hover {{ transform: scale(1.02); filter: brightness(1.2); }}
        .error {{ color: #ff4a4a; text-align: center; font-size: 13px; margin-bottom: 15px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Secure Login</h2>
        {"<p class='error'>⚠ " + msg + "</p>" if msg else ""}
        <form method="POST">
            <label>Username</label><input type="text" name="u" placeholder="Admin ID" required autocomplete="off">
            <label>Password</label><input type="password" name="p" placeholder="••••••••" required>
            <button type="submit">AUTHENTICATE SYSTEM</button>
        </form>
    </div>
</body>
</html>"""