from flask import Flask, render_template, request, session, redirect
from quize_question import questions

app = Flask(__name__)

app.secret_key = "quiz_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/category")
def category():
    return render_template("category.html")


@app.route("/difficulty/<category>")
def difficulty(category):
    return render_template(
        "difficulty.html",
        category=category
    )


@app.route("/quiz/<category>/<difficulty>", methods=["GET", "POST"])
def quiz(category, difficulty):

    category_questions = questions.get(category, [])

    selected_questions = [
        q for q in category_questions
        if q["difficulty"] == difficulty
    ]

    if not selected_questions:
        return "No questions found."


    # Start quiz
    if "quiz_index" not in session:
        session["quiz_index"] = 0
        session["score"] = 0


    index = session["quiz_index"]


    # Check submitted answer
    if request.method == "POST":

        answer = request.form.get("answer")

        correct_answer = selected_questions[index]["answer"]

        if answer == correct_answer:
            session["score"] += 1

        session["quiz_index"] += 1


        # Quiz finished
        if session["quiz_index"] >= len(selected_questions):

            score = session["score"]

            total = len(selected_questions)

            percentage = (score / total) * 100


            # Clear quiz session
            session.pop("quiz_index")
            session.pop("score")


            return render_template(
                "result.html",
                score=score,
                total=total,
                percentage=percentage,
                category=category,
                difficulty=difficulty
            )


        return redirect(
            f"/quiz/{category}/{difficulty}"
        )


    # Show current question
    question = selected_questions[index]


    return render_template(
        "quize.html",
        question=question,
        question_number=index + 1,
        total_questions=len(selected_questions),
        category=category,
        difficulty=difficulty
    )


if __name__ == "__main__":
    app.run(debug=True)