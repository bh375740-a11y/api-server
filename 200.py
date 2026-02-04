from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Gannuhacker Free API</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            padding: 20px;
        }
        pre {
            white-space: pre-wrap;
        }
    </style>
</head>
<body>

<pre>
=========================================
  WHITE HACKER SUPPORT 
 But Hum Free Me Dete Hai 🙌❤️
=========================================

        ⚠️  GANNU HACKER ⚠️

     📌 DANGER  NOTIFICATION 🛑
       

1️⃣ PHONE NUMBER LOOKUP:
   /number/9876543210

2️⃣ AADHAAR NUMBER LOOKUP:
   /aadhaar/123412341234

3️⃣ EMAIL LOOKUP:
   /email/test@example.com

4️⃣ AUTO-DETECT SEARCH:
   /search/your_query

-----------------------------------------


-----------------------------------------

⚠️ DISCLAIMER:
• Educational purpose only

       ❌❌❌

=========================================
 ● Credit   : Gannuhacker
 ● Developer: Gannu Hacker
=========================================
</pre>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)