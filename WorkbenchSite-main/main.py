from flask import Flask
from data import db_session
from data.cards import Card



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()
    card = Card()

    card.title = "Худи Omegaaaasdkeklsul"
    card.content = "Хлопок"
    card.price = "1700"
    card.filename = "static/images/bot.jpg"
    card.key_words = "одежда"

    db_sess.add(card)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
