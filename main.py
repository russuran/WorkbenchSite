from flask import Flask
from data import db_session
from data.cards import Card
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()
    user = User()

    user.name = "admin"
    user.about = "admin"
    user.email = "a@a.a"
    user.hashed_password = "123"

    db_sess.add(user)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
