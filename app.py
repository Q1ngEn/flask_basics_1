from flask import Flask, render_template
import random

app = Flask(__name__)

my_college = 'ASRJC'
rival_college = 'ACJC'
secret_text = 'Never gonna give you up. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and desert you'
secret_nums = [1111, 7722, 2, 991122334455667788]
secret_info = {"name": "Qing En", "Descripttion": "Stupid", "gender": "Male", "type": "human"}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/h2comp")
@app.route("/best_subject")
@app.route("/computing")
def computing():
    return "<h1> What is computing?<h1>"

@app.route("/about")
def about():
    return render_template("about.html", my_college=my_college, rival_college=rival_college)

@app.route('/secret')
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template('secret.html', secret_text=secret_text, lucky_num=lucky_num, secret_info=secret_info)

if __name__ == "__main__":
    app.run(debug=True)
