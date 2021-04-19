from flask import Flask, url_for, request, render_template, redirect, make_response, jsonify
from forms.loginform import LoginForm
from data.cards import Card
from data.users import User
from forms.user import RegisterForm
from data import db_session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from random import shuffle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OmaewaMouShindeeru'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return redirect('/main/a/a/a')


@app.route('/main/<theme>/<under_theme>/<material>')
def main(theme, under_theme, material):

    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()

    if theme == "a":
        card = db_sess.query(Card)
    else:
        card = db_sess.query(Card).filter(Card.theme == theme,
                                          Card.under_theme == under_theme,
                                          Card.material == material)


    return render_template('shoppings.html', cards=card, length=card.count())

@app.route('/main/<theme>/<under_theme>/product/<id>')
def product(theme, under_theme, id):
    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()
    data = db_sess.query(Card).filter(Card.id == id).first()
    return render_template('product.html', data=data)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_session.global_init("db/cards.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/main/a/a/a")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/about')
def about():
    return render_template('about_us.html')


@app.route('/support/<part>')
def support(part):

    return render_template('support.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Server Error'}), 500)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
