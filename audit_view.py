import os

def get_page():
    logs = []
    if os.path.exists("audit_history.log"):
        with open("audit_history.log", "r") as f:
            logs = f.readlines()

    # Log डेटाला टेबल रो मध्ये कन्व्हर्ट करणे
    log_rows = ""
    for log in logs:
        # रंगीत कोडिंगसाठी (उदा. ENCRYPT साठी निळा, DECRYPT साठी हिरवा)
        color = "#00d2ff" if "ENCRYPT" in log else "#00ff9d"
        log_rows += f"<tr style='color: {color}; border-bottom: 1px solid #333;'><td>{log.strip()}</td></tr>"

    return f"""
    <html>
    <head>
        <style>
            body {{ background: #050505; color: #fff; font-family: 'Courier New', monospace; padding: 40px; }}
            .container {{ max-width: 900px; margin: auto; background: #111; padding: 30px; border-radius: 15px; border: 1px solid #333; }}
            h2 {{ color: #00d2ff; text-transform: uppercase; letter-spacing: 2px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            td {{ padding: 10px; font-size: 14px; }}
            .btn {{ 
                display: inline-block; padding: 12px 20px; background: #333; color: #fff; 
                text-decoration: none; border-radius: 5px; margin-top: 20px; transition: 0.3s; 
            }}
            .btn:hover {{ background: #00d2ff; color: #000; }}
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/dashboard" style="color: #666; text-decoration: none;">&larr; Back to Dashboard</a>
            <h2>🛡️ System Audit Logs</h2>
            <div style="height: 400px; overflow-y: auto; background: #000; padding: 15px; border-radius: 10px;">
                <table>
                    {log_rows}
                </table>
            </div>
            <a href="/download-log" class="btn">📥 Download Raw Log (.log)</a>
        </div>
    </body>
    </html>
    """