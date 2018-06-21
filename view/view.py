from flask import Flask,request

app = Flask(__name__)

@app.route('/graphical')
def graphical():
    returnValue = 'hello' if request.args.get('data') == None else request.args.get('data')
    return returnValue