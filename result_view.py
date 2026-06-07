from theme_styles import COMMON_CSS
import crypto_engine

def get_page(orig, algo, res, strength, mode):
    # १. स्ट्रेंथ बारसाठी कलर लॉजिक
    color = "#ff4a4a" if strength < 40 else "#ffaa00" if strength < 80 else "#00e676"
    
    # २. नवीन फीचर्स
    salt = crypto_engine.generate_salt()
    entropy = crypto_engine.get_entropy(orig)
    is_valid = "✅ Strong Key" if crypto_engine.validate_custom_key(orig) else "⚠️ Needs Improvement"
    
    # ३. अटॅक मॅट्रिक्स टेबल
    attacks = crypto_engine.get_detailed_attack_analysis(orig)
    rows = "".join([f"<tr style='border-bottom:1px solid #222;'><td style='padding:8px;font-size:12px;color:#aaa;'>{name}</td><td style='padding:8px;font-size:12px;color:{'#ff4a4a' if 'Instant' in timing else '#00e676'};'>{timing}</td></tr>" for name, timing in attacks.items()])

    return f"""<html>
<head>
    <title>Page 3 - Security Audit Result</title>
    {COMMON_CSS}
    <script>
        function copyText() {{ var t = document.getElementById("outBox"); t.select(); navigator.clipboard.writeText(t.value); alert("Copied!"); }}
    </script>
</head>
<body>
    <div class="container" style="max-width:800px; margin: 30px auto; padding: 20px;">
        <h2 style="color:#ffaa00;">Cryptographic Audit Result</h2>
        
        <div style="background:#141414; padding:15px; border-radius:8px; margin-bottom:20px; border:1px solid #333;">
    <label style="color:#ffffff; font-weight:bold;">Security Strength Rating:</label>
    <div style="width:100%; background:#222; height:15px; border-radius:10px; margin:10px 0; border: 1px solid #444;">
        <div style="width:{strength}%; background:{color}; height:15px; border-radius:10px; transition:1s;"></div>
    </div>
    <p style="color:#ffffff; font-weight:bold; font-size:14px;">
        Score: <span style="color:{color};">{strength}/100</span> | 
        Entropy: <span style="color:#00d2ff;">{entropy} Bits</span>
    </p>
    </div>

        <div style="background:#0a0a0a; padding:15px; border-radius:8px; border:1px solid #333; margin-bottom:20px;">
            <p style="margin:5px 0; font-size:12px;"><strong>Key Salt:</strong> <span style="color:#00d2ff; font-family:monospace;">{salt}</span></p>
            <p style="margin:5px 0; font-size:12px;"><strong>Key Status:</strong> <span style="color:#eee;">{is_valid}</span></p>
        </div>
        
        <label>Cryptographic Output:</label>
        <textarea id="outBox" rows="3" style="color:#00e676;font-family:monospace;background:#050505!important; width:100%;" readonly>{res}</textarea>
        
        <div style="margin-top:20px; overflow-x: auto;">
            <h4 style="color:#00d2ff; margin-bottom:10px;">🛡️ Threat Resistance Analysis</h4>
            <table style="width:100%; min-width: 500px; border-collapse:collapse; background:#1a1a1a;">
                <thead><tr style="background:#222;"><th style="padding:8px;font-size:11px;text-align:left;">ATTACK TYPE</th><th style="padding:8px;font-size:11px;text-align:left;">RESISTANCE TIME</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>

        <div style="display:flex;gap:10px;margin-top:20px;">
            <button onclick="copyText()" style="background:#333;color:white;border:none;padding:10px;flex:1;cursor:pointer;">Copy Output</button>
            <a href="/export-report/{orig}/{algo}/{res.replace('/', '_')}" class="btn" style="background:#ffaa00;color:black;text-align:center;flex:1;text-decoration:none;padding:10px;">Download PDF Report</a>
            <a href="/dashboard" class="btn" style="background:rgba(255,255,255,0.1);color:white;text-align:center;flex:1;text-decoration:none;padding:10px;">Back</a>
        </div>
    </div>
</body>
</html>"""