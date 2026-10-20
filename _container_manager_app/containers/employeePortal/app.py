from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)


LOGIN_LOGS = [
    {"username": "j.smith", "password": "Summer2026", "status": "failed"},
    {"username": "mdingus", "password": "password123", "status": "failed"},
    {"username": "accounting", "password": "Welcome01", "status": "failed"},
    {"username": "hr.manager", "password": "Spring2026", "status": "failed"},
    {"username": "admin", "password": "KeysToTheCyb3rC1ty", "status": "success"},
    {"username": "doctorate", "password": "letmein123", "status": "failed"},
    {"username": "support", "password": "Support2026", "status": "failed"},
]

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Portal</title>
</head>
<body>
    <h1>Employee Login</h1>

    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required>

        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>

        <br><br>

        <button type="submit">Login</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}

    <script>
        // Simulates a background request made by the employee portal.
        // Inspect its response in Burp Suite HTTP history.
        fetch("/api/activity");
    </script>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == "admin" and password == "KeysToTheCyb3rC1ty":
            return render_template_string(
                LOGIN_PAGE,
                message="Login successful! The flag is CTF{PWNED}"
            )

        return render_template_string(
            LOGIN_PAGE,
            message="Invalid credentials."
        )

    return render_template_string(LOGIN_PAGE, message=None)


@app.route("/api/activity")
def activity():
    return jsonify({"recent_login_activity": LOGIN_LOGS})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)