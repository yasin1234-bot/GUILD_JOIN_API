from flask import Flask, render_template

web_app = Flask(__name__)

@web_app.route("/")
def index():
    return render_template("index.html")

# Vercel এন্ট্রি পয়েন্ট
app = web_app

if __name__ == "__main__":
    web_app.run(debug=False, host='0.0.0.0', port=5002)