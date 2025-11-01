from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user data (in real case, use database)
users = {"testuser": "1234"}
posts = []

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            return redirect(url_for('feed'))
        else:
            return "Invalid credentials! Try again."
    return render_template('login.html')

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if request.method == 'POST':
        new_post = request.form.get('content')
        posts.append(new_post)
    return render_template('feed.html', posts=posts)

@app.route('/profile')
def profile():
    return render_template('profile.html', username="testuser")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
