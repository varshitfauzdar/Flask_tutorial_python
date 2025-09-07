from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
    return "Hello, World!"

@app.route('/about')
def about():
    return "hyy I am Varshit Fauzdar"
    
@app.route('/success/<int:score>')  #here score is a parameter
def success(score):
    return "cheetah hi khde....bhai ke poore " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Aww lele babu fail hogya...kitne aae " + str(score)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
