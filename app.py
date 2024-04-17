from flask import Flask, render_template

from src.chiffres import draw_numbers, solve_lceb
from src.lettres import draw_letters, solve_lmlpl
from src.utils import load_config

app = Flask(__name__)
config = load_config()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/numbers")
def numbers_game():
    numbers, target = draw_numbers()
    solution = solve_lceb(numbers, target)
    solution_str = "<br>".join(solution)
    return render_template(
        "numbers.html",
        numbers=numbers,
        target=target,
        solution=solution_str,
        timers=config["numbers"],
    )


@app.route("/letters")
def letters_game():
    letters = draw_letters()
    solution = solve_lmlpl(letters)
    return render_template(
        "letters.html", letters=letters, solution=solution, timers=config["letters"]
    )


if __name__ == "__main__":
    app.run(debug=True)
