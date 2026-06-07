from flask import Flask, request, redirect, url_for, render_template_string, send_file
import os, webbrowser
import decrypt_page 
import dashboard_view
from threading import Timer
from datetime import datetime
from fpdf import FPDF

# Import View Engine modules
import login_view, result_view, decrypt_view, audit_view, encryption_page
import crypto_engine, decrypt_engine

app = Flask(__name__)

def append_log(action, algo, size):
    with open("audit_history.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {action} | Scheme: {algo.upper()} | Payload Size: {size} Chars\n")

@app.route('/')
def root(): 
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('u') == 'admin' and request.form.get('p') == 'admin':
            return redirect(url_for('encryption')) 
        return "Invalid Credentials"
    return render_template_string(login_view.get_page())

@app.route('/encryption', methods=['GET', 'POST'])
def encryption():
    if request.method == 'POST':
        payload = request.form.get('text')
        selected_algo = request.form.get('algo')
        
        if not payload or not selected_algo:
            return "Error: Missing Data", 400
            
        encrypted_result = crypto_engine.run_encrypt(payload, selected_algo)
        append_log("ENCRYPT", selected_algo, len(payload))
        
        # result_view.get_page चे ५ आर्गुमेंट्स आहेत असे गृहीत धरले आहे
        return render_template_string(result_view.get_page(payload, selected_algo, encrypted_result, 0, "Encryption"))
    
    return render_template_string(encryption_page.get_page())

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        payload = request.form.get('text')
        algo = request.form.get('algo')
        decrypted_result = crypto_engine.run_decrypt(payload, algo)
        return render_template_string(result_view.get_page(payload, algo, decrypted_result, 0, "Decryption"))
    
    return render_template_string(decrypt_page.get_page())
@app.route('/dashboard')
def dashboard():
    # Define navigation bar as a string
    nav_bar = """
    <div style="background:#1a1a1a; padding:15px; text-align:center; border-bottom:2px solid #00d2ff;">
        <a href="/encryption" style="margin:0 15px; color:#fff; text-decoration:none;">Encryption</a>
        <a href="/decrypt" style="margin:0 15px; color:#fff; text-decoration:none;">Decryption</a>
        <a href="/audit-logs" style="margin:0 15px; color:#fff; text-decoration:none;">Audit Logs</a>
    </div>
    """
    return nav_bar + dashboard_view.get_page()
    return nav_bar + dashboard_view.get_page()

@app.route('/audit-logs')
def audit_logs(): 
    return render_template_string(audit_view.get_page())

@app.route('/download-log')
def download_log():
    return send_file("audit_history.log", as_attachment=True)

if __name__ == '__main__':
    # १५०० मिलिसेकंद (१.५ सेकंद) चा वेळ दिला आहे, तो थोडा वाढवून २ सेकंद (२०००) करून बघ
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")
    
    Timer(2.0, open_browser).start() 
    app.run(debug=True, port=5000)