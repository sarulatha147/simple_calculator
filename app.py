from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        m1 = int(request.form["m1"])
        m2 = int(request.form["m2"])
        m3 = int(request.form["m3"])

        total = m1 + m2 + m3
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        result = {
            "name": name,
            "total": total,
            "average": round(average, 2),
            "grade": grade
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)