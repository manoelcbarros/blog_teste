from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')

db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()  # Busca no banco de dados os posts. Todos os posts
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    user = User(username='manolo', email="manolo@email.com", password_hash = 'a')
    post1 = Post(title="Bonaire", body="O Bonaire (em neerlandês: Bonaire; em papiamento: Boneiru) é um município especial (bijzondere gemeente) dos Países Baixos, antigamente um dos constituintes das Antilhas Neerlandesas, situada no mar das Caraíbas (mar do Caribe) ao largo da costa da Venezuela.", author="Manolo")
    post2 = Post(title="Império Romano", body="O Império Romano (em latim: Imperium Romanum[nt 3]) foi o período pós-republicano da antiga civilização romana,  caracterizado por uma forma de governo autocrática liderada por um imperador e por extensas possessões territoriais em volta do mar Mediterrâneo na Europa, África e Ásia.", author="Manolo")
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for('index'))