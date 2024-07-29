from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  #имя проектаё#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'#создаем базу данных после ///пишем название#
db = SQLAlchemy(app)


class Post(db.Model): #создаем класс#
    id = db.Column(db.Integer, primary_key=True)#1 штука -это тип данных ,вторая штука это подсчет пользователей#
    title = db.Column(db.String(300), nullable=False)#после String у нас есть цифра ,она разрешает нужное количество символов#
    text = db.Column(db.Text, nullable=False)#текст#


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    posts = Post.query.all()  #достаем все посты из базы данных#
    return render_template("posts.html",posts=posts)







@app.route('/gog', methods=["GET", "POST"])   #клвдем инфу в базу данных#
def about():
    if request.method == "POST":
       title = request.form['title']
       text = request.form['text']


       post = Post(title=title, text=text)

       try:
           db.session.add(post)
           db.session.commit()
           return redirect('/')
       except:                      #если будет ошибка#
           return 'При добовлении статьи произошла ошибка'
    else:
       return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
