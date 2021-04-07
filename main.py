from flask import Flask
from data import db_session
from data.cards import Card


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/cards.db")
    card = Card()
    with open("static/images/Spoon.jpg", "rb") as image:
        f = image.read()


    card.tite = "Spoon"
    card.content = "Алюминиевая ложка"
    card.price = "300"
    card.photo = f
    db_sess = db_session.create_session()
    db_sess.add(card)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
