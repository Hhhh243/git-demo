from flask import Flask,render_template,request
app = Flask(__name__)
date=[{'id':0,'name':'中秋节','num':0},
      {'id':1,'name':'春节','num':0},
      {'id':2,'name':'国庆节','num':0}]
@app.route('/index')
def index():
    return render_template('index2.html',date=date)
@app.route('/dianzan')
def dianzan():
    id=request.args.get('id')
    print('想要给{id}点赞!')
    date[int(id)]['num']+=1
    return render_template('index2.html',date=date)
app.run(debug=True)