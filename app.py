from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello, World!"

@app.route('/about')
def about():
    return "hyy I am Varshit Fauzdar"

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
