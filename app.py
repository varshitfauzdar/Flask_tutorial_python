from flask import Flask,render_template,request,redirect,url_for,jsonify
 

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

@app.route('/login',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('login_page.html')


@app.route('/form',methods=['GET','POST'])
def form_tut():
    if request.method == 'GET':
        return render_template('form_tut.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average = (maths + science + history) / 3

        result = ""
        if average >= 50:
            result = "success"
        else:
            result = "fail"

        return redirect(url_for(result,score=average))
        # return render_template('form_tut.html',score=average)

@app.route('/api',methods=['POST'])     #use postman to test the api
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])

    return jsonify({'sum':a_val+b_val})



if __name__ == '__main__':
    app.run(debug=True, port = 8000)
