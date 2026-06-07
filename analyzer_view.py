from theme_styles import COMMON_CSS
def get_page(msg="", out=""):
    res_tag = f"<div style='background:rgba(0,210,255,0.1);padding:10px;border-radius:6px;text-align:center;color:#ffaa00;font-weight:bold;'>Analysis: {out}</div>" if out else ""
    return f"""<html><head><title>Page 9 - Analyzer</title>{COMMON_CSS}</head><body><div class="container">
    <h2>Page 9: Vulnerability & Password Analyzer</h2>
    <form method="POST"><label>Enter Password / Token to Test:</label><input type="text" name="pass_val" required placeholder="Type something..." autocomplete="off">
    <button type="submit">Analyze Entropy Strength</button></form>{res_tag}<br>
    <a href="/dashboard" class="btn" style="background:#333;">← Back to Control Panel</a></div></body></html>"""