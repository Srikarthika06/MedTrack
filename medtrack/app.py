from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to MedTrack"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "Registration Successful"
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("dashboard.html")
    return render_template("login.html")

@app.route("/book_appointment", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        return "Appointment Booked Successfully"
    return render_template("book_appointment.html")

@app.route("/view_appointments")
def view_appointments():
    appointments = [
        {"patient": "John Doe", "doctor": "Dr. Smith", "date": "2026-06-20", "time": "10:00 AM"}
    ]
    return render_template("view_appointments.html", appointments=appointments)

@app.route("/profile")
def profile():
    user = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "role": "Patient"
    }
    return render_template("profile.html", user=user)

@app.route("/submit_diagnosis", methods=["GET", "POST"])
def submit_diagnosis():
    if request.method == "POST":
        return "Diagnosis Submitted Successfully"
    return render_template("submit_diagnosis.html")

@app.route("/search_appointments", methods=["GET", "POST"])
def search_appointments():
    results = []
    if request.method == "POST":
        results = [
            {"patient": "John Doe", "doctor": "Dr. Smith", "date": "2026-06-20", "status": "Confirmed"}
        ]
    return render_template("search_appointments.html", results=results)

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True)