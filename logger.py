from datetime import datetime
def log_action(action, algo, text_len):
    with open("audit_history.log", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action} | Scheme: {algo} | Size: {text_len} chars\n")