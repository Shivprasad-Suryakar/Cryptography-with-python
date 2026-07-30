# पायथनची अधिकृत इमेज वापरा
FROM python:3.9-slim

# कंटेनरमध्ये काम करण्याची डिरेक्टरी सेट करा
WORKDIR /app

# गरजू फाइल्स कंटेनरमध्ये कॉपी करा
COPY . .

# जर तुमच्याकडे requirements.txt असेल तर ती इंस्टॉल करा
# (जर नसेल तर ही ओळ काढून टाका)
RUN pip install --no-cache-dir -r requirements.txt || echo "requirements.txt not found"

# तुमची मुख्य पायथन फाइल रन करा (उदा. main.py)
# तुमच्या फाइलचे नाव वेगळे असेल तर 'main.py' ऐवजी ते नाव द्या
CMD ["python", "main.py"] 
