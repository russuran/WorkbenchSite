from flask import Flask, url_for, request, render_template, redirect
from forms.loginform import LoginForm, RegisterForm
from data.cards import Card
from data.users import User
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
    print(type(theme), under_theme, material)

    db_session.global_init("db/cards.db")
    db_sess = db_session.create_session()

    if theme == "a":
        card = db_sess.query(Card)
    else:
        card = db_sess.query(Card).filter(Card.theme == theme,
                                          Card.under_theme == under_theme,
                                          Card.material == material)

    return render_template('shoppings.html', cards=card, length=card.count())

@app.route('/product/<id>')
def product(id):
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
        return redirect('/')
    return render_template('login.html', form=form)


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

@app.route('/about')
def about():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
