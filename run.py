from quizapp import app, db
from seed_words import seed_words, SEED_RESET

if __name__ == "__main__":
    with app.app_context():
        if SEED_RESET:
            seed_words()  # feltölti a Word táblát

    app.run(debug=True)