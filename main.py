from flask import Flask
from data import db_session
from data.cards import Card
from data.users import User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()

    user = User()
    user.name = "r"
    user.about = "r"
    user.email = "rr@gmail.com"
    user.password = "r"
    db_sess.add(user)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
