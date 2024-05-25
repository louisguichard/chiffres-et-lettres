from flask import Flask, render_template, request
import yaml

from src.chiffres import draw_numbers, solve_lceb
from src.lettres import draw_letters, solve_lmlpl

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/config", methods=["GET"])
def get_config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config


@app.route("/config", methods=["POST"])
def save_config():
    config = request.json
    with open("config.yaml", "w") as file:
        yaml.safe_dump(config, file)
    return "", 204


@app.route("/numbers")
def numbers_game():
    config = get_config()
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
    config = get_config()
    letters = draw_letters()
    solution = solve_lmlpl(letters)
    return render_template(
        "letters.html", letters=letters, solution=solution, timers=config["letters"]
    )


if __name__ == "__main__":
    app.run()
