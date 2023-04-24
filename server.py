from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import wikipy, wikipedia

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)

@app.route('/')
def index():
    return render_template('client.html')

@socket.on('send list')
def handle_search_list(data):
    searchWord = data['searchKey']
    Lists = wikipy.search_list(searchWord)
    emit("list response",Lists)

@socket.on('select')
def handle_select(data):
    searchKey = data['searchKey']
    index = data['index']
    summary, disambiguation, image_url, url = wikipy.search_wiki(searchKey,index)
    if(disambiguation):
            emit('disambi',summary)
    else:
        message = f'Summary: {summary}'
        emit('message',{'message': message, 'image': image_url, 'url': url})

@socket.on('disambiSelect')
def handle_disambi(data):
     searchKey = data['searchKey']
     index = data['index']
     summary, disambiguation, image_url, url = wikipy.search_wiki(searchKey, index)
     if(disambiguation):
        emit('disambi',summary)
     else:
        message = f'Summary: {summary}'
        emit('message',{'message': message, 'image': image_url, 'url': url})


if __name__ == "__main__":
    socket.run(app,host="localhost",port=5000)
 
