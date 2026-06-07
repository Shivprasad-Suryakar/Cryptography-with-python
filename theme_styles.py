COMMON_CSS = """
<style>
    :root {
        --bg-color: #0a0a0a;
        --card-bg: #121212;
        --accent: #00d2ff;
        --text: #e0e0e0;
    }
    body { 
        background-color: var(--bg-color); 
        color: var(--text); 
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
        transition: all 0.3s ease;
    }
    .main-content {
        background: var(--card-bg);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #333;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    .main-content:hover { transform: scale(1.01); }
    
    textarea, select {
        width: 100%;
        padding: 15px;
        background: #1a1a1a;
        color: var(--accent);
        border: 1px solid #444;
        border-radius: 8px;
        transition: border 0.3s, box-shadow 0.3s;
    }
    textarea:focus, select:focus {
        border-color: var(--accent);
        box-shadow: 0 0 10px rgba(0,210,255,0.2);
        outline: none;
    }
    button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        padding: 15px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        width: 100%;
        transition: filter 0.3s;
    }
    button:hover { filter: brightness(1.2); }
</style>
"""