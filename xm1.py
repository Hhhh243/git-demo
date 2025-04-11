from flask import Flask,render_template
from random import randint
app = Flask(__name__)

hero=['a','b','c','d','e','f','g','h'
    ,'i','j','k','l','m','n','o','p', 'r']


@app.route('/index')
def index():
    return render_template('index.html',heros=hero)
@app.route('/choujiang')
def choujiang():
    num=randint(0,len(hero)-1)
    return render_template('index.html',heros=hero,h=hero[num])


app.run(debug=True)

