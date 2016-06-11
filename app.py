#coding=utf-8
from flask import Flask
from flask import request
from flask import current_app
from flask import g
from flask import make_response
import json

app = Flask(__name__)

notes = []

@app.route('/')
def tmp():
    return 'hello'

@app.route('/index')
def index():
    #requried_str = request.args['name']
    not_requried_str = request.args.get('name','no name')
    tmp = not_requried_str
    return '<h1>hello %s</h1>' % tmp

@app.route('/test/<name>')
def test(name):
    print 'input string:',name
    name = request.headers.get('User-Agent')
    print current_app.name
    return '<h1>your browser::%s </h1>' % name

@app.route('/add_note',methods=['POST','PUT'])
def add_note():
    title = request.form['title']
    notes.append(title)
    return title

@app.route('/notes')
def note():
    return json.dumps(notes)

@app.route('/res')
def res():
    res = make_response('<h1>carris a cookie</h1>')
    res.set_cookie('my_cookie','xiaoyan xiaoyan')
    return res,404,{"my_cookie2":"hahahaha"}
    #return 'haha custom response',404

@app.route('/delete',methods=['DELETE'])
def delete():
    name = request.form['title']
    notes.remove(name)
    return "%s is deleted" % name

if __name__ in '__main__':
    app.run(debug=True,host='0.0.0.0')
