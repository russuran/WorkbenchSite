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
    card.rating = "0"

    db_sess.add(card)
    db_sess.commit()

    card = Card()

    card.title = 'Лампа "CwB"'
    card.content = "Если у вашего рабочего места не хватает света и вкуса, то эта лампа специально для вас!"
    card.price = "2400"
    card.filename = "static/images/lamp_table.jpg"
    card.theme = "Декоративные предметы"
    card.under_theme = "Лампы"
    card.material = "Настольные"
    card.key_words = "Лампа"
    card.rating = "0"

    db_sess.add(card)
    db_sess.commit()

    card = Card()

    card.title = 'Лампа "BwC"'
    card.content = "Вам нужен свет и стиль? ВОТ ОН!"
    card.price = "3200"
    card.filename = "static/images/lamp_wall.jpg"
    card.theme = "Декоративные предметы"
    card.under_theme = "Лампы"
    card.material = "Настенные"
    card.key_words = "Лампа"
    card.rating = "0"

    db_sess.add(card)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
