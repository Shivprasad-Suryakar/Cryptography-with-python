from theme_styles import COMMON_CSS
def get_vulnerability_warning(algo):
    warnings = {
        'md5': "⚠️ VULNERABILITY: MD5 is cryptographically broken. Prone to Collision Attacks.",
        'sha1': "⚠️ VULNERABILITY: SHA-1 is deprecated and susceptible to collision attacks.",
        'sha256': "✅ STATUS: Currently secure and industry standard for data integrity.",
        'sha512': "✅ STATUS: Highly secure, resistant to collision and pre-image attacks.",
        'aes': "✅ STATUS: Military-grade security. Resistant to almost all known attacks.",
        'fernet': "✅ STATUS: Secure implementation of AES-128 with integrity verification.",
        'des': "❌ VULNERABILITY: Legacy DES has short 56-bit keys. Easily brute-forced.",
        '3des': "⚠️ VULNERABILITY: Deprecated. Vulnerable to 'Sweet32' birthday attacks.",
        'blowfish': "⚠️ STATUS: Secure, but slow with large keys. Replaced by AES.",
        'caesar': "❌ VULNERABILITY: Extremely weak. Zero protection against frequency analysis.",
        'reverse': "❌ VULNERABILITY: Obfuscation only. Not a cryptographic security measure.",
        'base64': "❌ VULNERABILITY: Encoding only, not encryption. Can be reversed instantly.",
        'base32': "❌ VULNERABILITY: Encoding only. Offers no data privacy.",
        'hex': "❌ VULNERABILITY: Data representation only. No protection against unauthorized access.",
        'url': "❌ VULNERABILITY: Simple formatting. Not secure for sensitive information."
    }
    return warnings.get(algo, "🛡️ STATUS: Algorithm status check not available.")
def get_page(orig_input="", selected_algo="all", single_result="", single_time=None, matrix_results=None):
    options_list = [
        ("all", "✨ ALL - Simultaneous Decryption Matrix"),
        ("caesar", "Caesar Shift Cipher"), ("reverse", "Reverse String Cipher"),
        ("fernet", "Fernet Private Token"), ("aes", "AES-256 Decryption"),
        ("des", "DES Block Legacy"), ("3des", "Triple DES (3DES)"), ("blowfish", "Blowfish Plain Cipher"),
        ("base64", "Base64 Decoder"), ("base32", "Base32 Decoder"), ("hex", "Hexadecimal to Plain"), ("url", "URL Percent Decoder"),
        ("md5", "MD5 Hash"), ("sha1", "SHA-1 Hash"), ("sha256", "SHA-256 Bit Hash"), ("sha512", "SHA-512 Bit Hash")
    ]
    
    dropdown_html = ""
    for val, name in options_list:
        sel = "selected" if selected_algo == val else ""
        dropdown_html += f'<option value="{val}" {sel}>{name}</option>'

    output_block = ""
    
    # CASE 1: सर्व १५ अल्गोरिदमचा डिफरेंशियल वेळ आणि आउटपुट मॅट्रिक्स दाखवणे
    if orig_input and selected_algo == "all" and matrix_results:
        table_rows = ""
        for algo, data in matrix_results.items():
            out = data['output']
            pc_t = data['pc_time']
            super_t = data['super_time']
            
            is_success = not any(x in out for x in ["❌", "🛡️"])
            text_color = "#00e676" if is_success else "#ff4a4a" if "🛡️" in out else "#555"
            row_bg = "background: rgba(0, 230, 118, 0.04);" if is_success else ""
            
            table_rows += f"""
            <tr style="{row_bg} border-bottom: 1px solid #222;">
                <td style="padding:10px; font-weight:bold; color:#00d2ff; font-size:12px; border-right:1px solid #222;">{algo}</td>
                <td style="padding:10px; font-family:monospace; color:{text_color}; font-size:12px; word-break:break-all; border-right:1px solid #222;">{out}</td>
                <td style="padding:10px; color:#ffaa00; font-size:11px; font-family:monospace; border-right:1px solid #222;">⏱️ {pc_t}</td>
                <td style="padding:10px; color:#ff3d00; font-size:11px; font-family:monospace;">⚡ {super_t}</td>
            </tr>"""
        
        output_block = f"""
        <label style="margin-top:25px; display:block;">DIFFERENTIAL ALG CRACK-TIME ANALYSIS MATRIX:</label>
        <div style="background:#141414; border:1px solid #333; border-radius:8px; overflow-x:auto; margin-bottom:20px;">
            <table style="width:100%; border-collapse:collapse; text-align:left; min-width:750px;">
                <thead>
                    <tr style="background:#1a1a1a; border-bottom:2px solid #333;">
                        <th style="padding:12px; color:white; font-size:11px; text-transform:uppercase; border-right:1px solid #333;">ALGORITHM SCHEME</th>
                        <th style="padding:12px; color:white; font-size:11px; text-transform:uppercase; border-right:1px solid #333;">DECRYPTED OUTPUT</th>
                        <th style="padding:12px; color:#ffaa00; font-size:11px; text-transform:uppercase; border-right:1px solid #333;">TIME (STANDARD PC)</th>
                        <th style="padding:12px; color:#ff3d00; font-size:11px; text-transform:uppercase;">TIME (SUPERCOMPUTER)</th>
                    </tr>
                </thead>
                <tbody>{table_rows}</tbody>
            </table>
        </div>"""
        
    # CASE 2: जर युझरने ड्रॉपडाउनमधून कोणताही १ विशिष्ट अल्गोरिदम निवडला असेल
    elif orig_input and single_result and single_time:
        text_color = "#ff4a4a" if any(x in single_result for x in ["❌", "🛡️"]) else "#00e676"
        output_block = f"""
        <div style="background: rgba(255,255,255,0.02); border: 1px solid #333; padding: 20px; border-radius: 10px; margin-top:25px;">
            <label>DECRYPTED PLAIN TEXT OUTPUT:</label>
            <textarea id="singleOut" style="color:{text_color}; font-family:monospace; font-size:15px; background:#050505!important; border-color:#222;" rows="3" readonly>{single_result}</textarea>
            
            <div style="display:flex; gap:15px; margin-top:15px; background:rgba(0,0,0,0.3); padding:10px; border-radius:6px; border:1px solid #222;">
                <div style="flex:1;"><span style="color:#aaa; font-size:11px;">Standard PC Crack Time:</span><br><strong style="color:#ffaa00; font-size:13px; font-family:monospace;">⏱️ {single_time[0]}</strong></div>
                <div style="flex:1;"><span style="color:#aaa; font-size:11px;">Supercomputer Crack Time:</span><br><strong style="color:#ff3d00; font-size:13px; font-family:monospace;">⚡ {single_time[1]}</strong></div>
            </div>
        </div>"""

    return f"""<html>
<head>
    <title>Page 4 - Time Matrix Workspace</title>
    {COMMON_CSS}
</head>
<body>
    <div class="container" style="max-width:850px;">
        <div class="nav-bar">
            <a class="nav-link" href="/dashboard">← Back to Dashboard</a>
            <span style="color:#ffaa00; font-size:12px; font-weight:bold;">Differential Complexity Active</span>
        </div>
        <h2 style="color:#ffaa00; text-shadow:0 0 10px rgba(255,170,0,0.2);">Decryption & Differential Time Analyzer</h2>
        <p style="text-align:center; color:#aaa; font-size:13px; margin-top:-10px;">Compare how much time different algorithms take to be cracked via Brute-Force</p>
        
        <form method="POST">
            <label>Step 1: Input Ciphertext / Secure Token / Raw Data</label>
            <textarea name="text" rows="2" placeholder="Paste data string here..." required>{orig_input}</textarea>
            
            <label>Step 2: Choose Decryption Target (Or select ALL to compare)</label>
            <select name="algo" required>
                {dropdown_html}
            </select>
            
            <button type="submit" style="background:linear-gradient(135deg, #ffaa00, #ff5500); color:black; font-weight:bold;">Analyze Differential Crack Times</button>
        </form>
        
        {output_block}
    </div>
</body>
</html>"""