from theme_styles import COMMON_CSS

def get_page():
    return f"""<html>
<head>
    {COMMON_CSS}
    <style>
        .dashboard-container {{ max-width: 1000px; margin: 40px auto; padding: 20px; }}
        .grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
            gap: 25px; 
            margin-top: 30px; 
        }}
        .card {{ 
            background: rgba(20, 20, 20, 0.9); 
            padding: 30px; 
            border-radius: 15px; 
            border: 1px solid #333; 
            text-align: center;
            transition: all 0.3s ease;
            text-decoration: none;
            color: #fff;
        }}
        .card:hover {{ 
            border-color: #00d2ff; 
            transform: translateY(-8px); 
            box-shadow: 0 10px 25px rgba(0, 210, 255, 0.15); 
        }}
        .icon {{ font-size: 3rem; margin-bottom: 15px; display: block; }}
        h2 {{ color: #00d2ff; text-align: center; margin-bottom: 10px; }}
        p.subtitle {{ text-align: center; color: #888; margin-bottom: 40px; }}
    </style>
</head>
<body>
    <div class="dashboard-container">
        <h2>Security Control Panel</h2>
        <p class="subtitle">Select a module to perform cryptographic operations</p>
        
        <div class="grid">
            <a href="/encryption" class="card">
                <span class="icon">🔐</span>
                <h3>Encryption</h3>
                <p>Advanced AES-256 and Symmetric cipher processing.</p>
            </a>
            
            <a href="/decrypt" class="card">
                <span class="icon">🔓</span>
                <h3>Decryption</h3>
                <p>Restore sensitive data using secure decryption keys.</p>
            </a>
            
            <a href="/audit-logs" class="card">
                <span class="icon">📜</span>
                <h3>Audit Logs</h3>
                <p>Track all encryption/decryption activity securely.</p>
            </a>
        </div>
    </div>
</body>
</html>"""