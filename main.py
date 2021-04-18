from flask import Flask
from data import db_session
from data.cards import Card



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()
    card = Card()

    card.title = 'Доска (Дуб)'
    card.content = "Качественная доска 5x1x0.3м"
    card.price = "1400"
    card.filename = "static/images/dub_wood.jpg"
    card.theme = "Материалы"
    card.under_theme = "Древесина"
    card.material = "Дубовая"
    card.key_words = "Доска"

    db_sess.add(card)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
