def analyze_strength(text):
    if len(text) < 6: return "Weak (Too Short)"
    score = sum([len(text) >= 10, any(c.isupper() for c in text), any(c.isdigit() for c in text), any(not c.isalnum() for c in text)])
    return "Medium Security" if score <= 1 else "Cyber-Grade Shield (Strong)"