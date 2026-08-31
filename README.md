I Deploy this Project through ECR (Elastic Container Registry) and (ECS Elastic Container Service) 


Linked In Link : https://lnkd.in/p/dF54GG6q


# 🔐 Cryptography-with-Python

एक प्रगत सुरक्षा आणि क्रिप्टोग्राफी डॅशबोर्ड, जो १५ पेक्षा जास्त एन्क्रिप्शन आणि डिक्रिप्शन अल्गोरिदमना सपोर्ट करतो.

## 🚀 फीचर्स
- **१५+ अल्गोरिदम:** AES-256, Fernet, DES, Triple DES, Blowfish, Base64, Caesar Shift, इ.
- **मॉडर्न UI:** डार्क-थीम आणि ग्लासमोर्फिझम आधारित प्रोफेशनल डॅशबोर्ड.
- **ऑडिट लॉगिंग:** सिस्टिममध्ये होणाऱ्या प्रत्येक एन्क्रिप्शन आणि डिक्रिप्शन क्रियेचे रिअल-टाइम ट्रॅकिंग.
- **ब्रूट-फोर्स अनॅलिसिस:** पासवर्डची ताकद आणि अटॅक वेळेचे विश्लेषण.
- **Drag & Drop:** सोप्या फाईल हाताळणीसाठी ड्रॅग आणि ड्रॉप सुविधा.

## 🛠️ तंत्रज्ञान (Technology Stack)
- **Backend:** Python (Flask Framework)
- **Security:** `cryptography`, `PyCryptodome`, `hashlib`
- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript

## 📦 इन्स्टॉलेशन
१. रिपॉझिटरी क्लोन करा:
   `git clone https://github.com/Shivprasad-Suryakar/Cryptography-with-python.git`

२. आवश्यक लायब्ररीज इन्स्टॉल करा:
   `pip install flask cryptography pycryptodome`

३. ॲप रन करा:
   `python main.py`

## 🛡️ सुरक्षा सूचना
ही सिस्टिम शैक्षणिक उद्देशाने (Educational Purpose) तयार केली आहे. संवेदनशील डेटासाठी नेहमी इंडस्ट्री-स्टँडर्ड एन्क्रिप्शन लायब्ररीजचा वापर करा.

## 👤 लेखक
Shivprasad Suryakar

1. Project Overview
Your project is a Web-Based Cryptographic Security Console built with Python and Flask. It allows users to perform various encryption and decryption operations using 15 different algorithms, track activities via logs, and analyze password security.

2. File Organization
Here is the structure of your project to keep your workflow organized:

**Frontend (Views):**

dashboard_view.py: The main landing page with cards.

encryption_page.py / decrypt_view.py: Input forms with drag-and-drop support.

result_view.py: Displays the output with copy-to-clipboard functionality.

audit_view.py: Displays system logs in a table format.

theme_styles.py: Contains the global CSS for a unified dark, "cyber" look.


**Backend (Engine):**

main.py: The Flask server that handles URL routing.

crypto_engine.py: Contains the logic for 15+ encryption algorithms.

decrypt_engine.py: Handles decryption logic for all algorithms.

logger.py: Manages the audit_history.log file.

validator.py: Ensures key strength and input integrity.


**3. Technologies Used**

Flask: Web framework for the server.

Cryptography & PyCryptodome: Core libraries for AES, DES, Blowfish, Fernet, etc.

Hashlib: For Hashing algorithms (MD5, SHA-256, etc.).

Standard Python Modules: secrets (for random salts), math (for brute-force timing), and os (for file handling).

https://lnkd.in/p/dF54GG6q
