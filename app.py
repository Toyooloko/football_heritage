from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
posts = [
    {
        'author': 'Toyo Oloko',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 22 2022',
    },
    {
        'author': 'Theo Filsell-bayes',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'November 21 2022',
    },
{
        'author': 'Ben Webb',
        'title': 'Blog Post 3',
        'content': 'First post content',
        'date_posted': 'November 20 2022',
    }
]
# home page the first page the user has access displaying recent posts and annoucements
@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html', posts=posts)
# about page talks about the contents of the website and its purpose
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='About')
# registration page used for new users to register an account with their email, username and password
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
# login page used for registered users to access their account
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
